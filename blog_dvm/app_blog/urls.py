from django.contrib import admin
from django.urls import path

from app_blog.views import *

urlpatterns = [
    path('subscribe/',subscribe, name = 'subscribe'),
    path('createuser/',create_user, name = 'create_user'),
    path('index/',index, name = 'index'),
    path('post/',post, name = 'post'),
    path('readpost/<post_post>',read_post, name = 'readpost'),
   
]