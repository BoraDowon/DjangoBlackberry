from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from comments.models import Comment


class IsCommentExists(permissions.BasePermission):
    def has_permission(self, request, view):
        comment_id = view.kwargs.get('comment_id')
        try:
            _ = Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            raise PermissionDenied({"message": "There is no commnet"})
        else:
            return True
