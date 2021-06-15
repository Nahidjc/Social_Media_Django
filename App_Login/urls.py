from django.urls import path, include
from App_Login import views

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),

]
