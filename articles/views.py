from django.http import HttpResponse, JsonResponse
from django.http import HttpRequest
from django.views.decorators import csrf

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from articles.models import Article
from articles.serializers import ArticleSerializer


@csrf.csrf_exempt
def article_list(request: HttpRequest):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
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
