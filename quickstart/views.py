from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from quickstart.models import Student
from quickstart.permissions import IsAdminOrReadOnly
from quickstart.serializers import StudentSerializer, UserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('name')
    serializer_class = StudentSerializer
    permission_classes = [IsAdminOrReadOnly]
