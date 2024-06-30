from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    """
    Разрешает доступ только пользователям из группы «Модераторы».
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name="moderator").exists()


class IsOwner(BasePermission):
    """
    Разрешает доступ только пользователям, которые являются владельцами объекта.
    """

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
