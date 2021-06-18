from django.urls import path, include
from App_Login import views


app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.login_page, name='login'),
    path('edit/', views.edit_profile, name='edit'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('user/<username>/', views.other_user, name='user'),

]
