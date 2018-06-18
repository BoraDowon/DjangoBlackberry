from django.http import HttpResponse, JsonResponse
from django.http import HttpRequest
from django.views.decorators import csrf

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from boards.models import Board
from boards.serializers import BoardSerializer


@csrf.csrf_exempt
def board_list(request: HttpRequest):
    if request.method == 'GET':
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        output = dict()
        output['data'] = serializer.data
        output['msg'] = 'SUCCESS'
        return JsonResponse(output, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BoardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
