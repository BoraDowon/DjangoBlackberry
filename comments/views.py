from django.http import HttpRequest

from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from comments.models import Comment
from comments.serializers import CommentSerializer
from comments.serializers import CommentListSerializer
from comments.permissions import IsCommentExists

from boards.permissions import IsBoardExists
from articles.permissions import IsArticleExists


class CommentList(APIView):
    permission_classes = (IsBoardExists, IsArticleExists, )
    lookup_board_kwarg = 'board_id'
    lookup_article_kwargs = 'article_id'

    def get(self, request: HttpRequest, board_id: int, article_id: int):
        comments = Comment.objects.all().filter(article_id=article_id)
        serializer = CommentListSerializer(comments, many=True)
        output = dict()
        output['data'] = serializer.data
        output['msg'] = 'SUCCESS'
        return Response(output, status=status.HTTP_200_OK)

    def post(self, request: HttpRequest, board_id: int, article_id: int):
        data = JSONParser().parse(request)
        data[self.lookup_article_kwargs] = article_id

        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            #serializer.save()
            comment = Comment()
            comment.add_root(
                contents=data['contents'],
                article_id=article_id
            )
            return Response({'mes': 'success'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):
    permission_classes = (IsBoardExists, IsArticleExists, IsCommentExists)
    lookup_board_kwarg = 'board_id'
    lookup_article_kwargs = 'article_id'
    lookup_comment_kwargs = 'comment_id'

    def post(self, request: HttpRequest, board_id: int, article_id: int, comment_id: int):
        data = JSONParser().parse(request)
        data[self.lookup_article_kwargs] = article_id

        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            # serializer.save()
            comment = Comment.objects.get(pk=comment_id)
            comment.add_child(
                contents=data['contents'],
                article_id=article_id
            )
            return Response({'mes': 'success'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: HttpRequest, board_id: int, article_id: int, comment_id: int):
        pass

    def delete(self, request: HttpRequest, board_id: int, article_id: int, comment_id: int):
        pass
