from django.urls import path
from articles import views

urlpatterns = [
    path('boards/<int:board_id>/articles/<int:article_id>/', views.ArticleDetail.as_view())
]
