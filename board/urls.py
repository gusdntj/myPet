from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:postId>/', views.detail, name='detail'),
    path('answer/create/<int:postId>/', views.answer_create, name='answer_create'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]