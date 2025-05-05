from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from quickstart.models import Student


class StudentAPITestCase(APITestCase):
    def setUp(self):
        # Создаем тестовых пользователей
        self.admin = User.objects.create_user(username='admin', password='adminpass', is_staff=True)
        self.regular_user = User.objects.create_user(username='user', password='userpass')

        # Создаем тестовые данные
        self.student_data = {
            'name': 'Test Student',
            'age': 1,
            # добавьте другие необходимые поля
        }
        self.student = Student.objects.create(**self.student_data)

        # URL для тестирования
        self.list_url = '/api/students/'
        self.detail_url = f'/api/students/{self.student.id}/'

    def get_client_with_token(self, user):
        """Возвращает клиент API с установленным токеном авторизации"""
        client = APIClient()
        client.force_authenticate(user)
        return client

    def test_anonymous_user_access(self):
        # Анонимные пользователи не должны иметь доступ
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.post(self.list_url, self.student_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_regular_user_safe_methods(self):
        client = self.get_client_with_token(self.regular_user)

        # GET list - должен быть доступен
        response = client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # GET detail - должен быть доступен
        response = client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_regular_user_unsafe_methods(self):
        client = self.get_client_with_token(self.regular_user)

        # POST - должен быть запрещен
        response = client.post(self.list_url, self.student_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # PUT - должен быть запрещен
        response = client.put(self.detail_url, self.student_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # DELETE - должен быть запрещен
        response = client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_user_all_methods(self):
        client = self.get_client_with_token(self.admin)

        # GET list - должен быть доступен
        response = client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # POST - должен быть доступен
        response = client.post(self.list_url, self.student_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # PUT - должен быть доступен
        updated_data = self.student_data.copy()
        updated_data['name'] = 'Updated Name'
        response = client.put(self.detail_url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # DELETE - должен быть доступен
        response = client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_student_creation(self):
        client = self.get_client_with_token(self.admin)
        new_student = {
            'name': 'New Student',
            'age': 10,
            # другие поля
        }
        response = client.post(self.list_url, new_student)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 2)  # 1 был создан в setUp, + этот

    def test_student_update(self):
        client = self.get_client_with_token(self.admin)
        updated_data = {
            'name': 'Updated Student',
            'age': 10,
        }
        response = client.put(self.detail_url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.student.refresh_from_db()
        self.assertEqual(self.student.name, 'Updated Student')
