from django.contrib import admin
from django.urls import path

from app_blog.views import *

urlpatterns = [
    path('index/',index, name = 'index'),
    path('post/',post, name = 'post'),
    path('readpost/<post_id>',read_post, name = 'readpost'),
    path('editpost/<post_id>',edit_post, name = 'editpost'),
    path('deletepost/<pk>',DeletePost.as_view(), name = 'deletepost'),
    path('about',about_the_author, name = 'about'),
   
]