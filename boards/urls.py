from django.urls import path
from boards import views

urlpatterns = [
    path('boards/<int:board_id>/', views.ArticleList.as_view())
]
