from rest_framework import permissions


class AuthorPermissions(permissions.BasePermission):
    """
    Предоставляет доступ безопасными методами к объекту
    и запрещает небезопасные, если запращивающий пользователь не
    создатель объекта
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
