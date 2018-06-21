from django.urls import path
from comments import views

urlpatterns = [
    path('boards/<int:board_id>/articles/<int:article_id>/comments/', views.CommentList.as_view()),
    path('boards/<int:board_id>/articles/<int:article_id>/comments/<int:comment_id>/', views.CommentDetail.as_view())
]
