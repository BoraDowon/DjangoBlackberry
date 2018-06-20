from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from articles.models import Article


class IsArticleExists(permissions.BasePermission):
    def has_permission(self, request, view):
        board_id = view.kwargs.get('board_id')
        article_id = view.kwargs.get('article_id')
        try:
            article = Article.objects.get(id=article_id)
        except Article.DoesNotExist:
            raise PermissionDenied({"message": "There is no article"})
        else:
            return article.board_id == board_id

