from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from boards.models import Board


class IsBoardExists(permissions.BasePermission):
    def has_permission(self, request, view):
        board_id = view.kwargs.get('board_id')
        try:
            _ = Board.objects.get(id=board_id)
        except Board.DoesNotExist:
            raise PermissionDenied({"message": "There is no board"})
        else:
            return True
