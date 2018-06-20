from django.http import HttpRequest

from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from boards.permissions import IsBoardExists

from articles.models import Article
from articles.serializers import ArticleSerializer
from articles.permissions import IsArticleExists


class ArticleDetail(APIView):
    permission_classes = (IsBoardExists, IsArticleExists,)
    lookup_board_kwarg = 'board_id'
    lookup_article_kwarg = 'article_id'

    def get(self, request: HttpRequest, board_id: int, article_id: int):
        article = Article.objects.get(id=article_id)
        serializer = ArticleSerializer(article)
        output = dict()
        output['data'] = serializer.data
        output['msg'] = 'SUCCESS'
        return Response(output, status=status.HTTP_200_OK)

    def put(self, request: HttpRequest, board_id: int, article_id: int):
        pass

    def delete(self, request: HttpRequest, board_id: int, article_id: int):
        pass
