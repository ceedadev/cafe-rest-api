from django.urls import path
from cafe_api import views

urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view())
]
