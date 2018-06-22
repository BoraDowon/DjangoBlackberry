from django.http import HttpRequest

from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.models import Berry
from accounts.serializers import BerrySerializer, BerryListSerializer


class BerryDetail(APIView):
    def get(self, request: HttpRequest, berry_id: int):
        berry = Berry.objects.get(pk=berry_id)
        serializer = BerrySerializer(berry)
        output = dict()
        output['data'] = serializer.data
        output['msg'] = 'SUCCESS'
        return Response(output, status=status.HTTP_200_OK)

    def put(self, request: HttpRequest, board_id: int, article_id: int):
        pass

    def delete(self, request: HttpRequest, board_id: int, article_id: int):
        pass


class BerryList(APIView):
    def get(self, request: HttpRequest):
        berries = Berry.objects.all()
        serializer = BerryListSerializer(berries, many=True)
        output = dict()
        output['data'] = serializer.data
        output['msg'] = 'SUCCESS'
        return Response(output, status=status.HTTP_200_OK)
