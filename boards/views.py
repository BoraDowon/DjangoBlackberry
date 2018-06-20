from django.http import HttpRequest

from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from boards.permissions import IsBoardExists

from articles.models import Article
from articles.serializers import ArticleSerializer
from articles.serializers import ArticleListSerializer


class ArticleList(APIView):
    permission_classes = (IsBoardExists,)
    lookup_board_kwarg = 'board_id'

    def get(self, request: HttpRequest, board_id: int):
        articles = Article.objects.all().filter(board_id=board_id)
        serializer = ArticleListSerializer(articles, many=True)
        output = dict()
        output['data'] = serializer.data
        output['msg'] = 'SUCCESS'
        return Response(output, status=status.HTTP_200_OK)

    def post(self, request: HttpRequest, board_id: int):
        data = JSONParser().parse(request)
        data[self.lookup_board_kwarg] = board_id

        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
