from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        # Разрешаем безопасные методы для всех аутентифицированных пользователей
        if not request.user:
            return False

        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        # Разрешаем небезопасные методы только для админов
        return request.user.is_authenticated and request.user.is_staff