from django.urls import path
from user_app import views

app_name = "user_app"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]