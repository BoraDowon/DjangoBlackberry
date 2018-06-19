from django.http import HttpResponse, JsonResponse
from django.http import HttpRequest
from django.views.decorators import csrf
from django.utils.decorators import method_decorator

from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from articles.models import Article
from articles.serializers import ArticleSerializer, ArticleListSerializer


@csrf.csrf_exempt
def article_list(request: HttpRequest, board_id: int):
    if request.method == 'GET':
        articles = Article.objects.all().filter(board_id=board_id)
        serializer = ArticleListSerializer(articles, many=True)
        output = dict()
        output['data'] = serializer.data
        output['msg'] = 'SUCCESS'
        return JsonResponse(output, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class ArticleList(APIView):
    @method_decorator(csrf.csrf_exempt)
    def get(self, request: HttpRequest, board_id: int):
        articles = Article.objects.all().filter(board_id=board_id)
        serializer = ArticleListSerializer(articles, many=True)
        output = dict()
        output['data'] = serializer.data
        output['msg'] = 'SUCCESS'
        return JsonResponse(output, safe=False)

    def post(self, request: HttpRequest, board_id: int):
        data = JSONParser().parse(request)
        article = Article(title=data['title'], body=data['body'], board_id=board_id)
        article.save()
        return JsonResponse({'msg': 'SUCCESS'}, status=201)
