from django.urls import path
from accounts import views

urlpatterns = [
    path('accounts/', views.BerryList.as_view()),
    path('accounts/<int:berry_id>/', views.BerryDetail.as_view()),
]
