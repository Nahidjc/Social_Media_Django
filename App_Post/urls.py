from django.contrib.staticfiles.urls import urlpatterns
from App_Post import views
from django.urls import path
app_name = 'App_Post'

urlpatterns = [
    path("", views.home, name='home'),
    path('liked/<pk>/', views.liked, name='liked'),
    path('unliked/<pk>/', views.unliked, name='unliked'),
]
