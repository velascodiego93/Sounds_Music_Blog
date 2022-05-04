from django.contrib import admin
from django.urls import path

from pages.views import *

urlpatterns = [
    path('',index, name = 'index'),
    path('post/',post, name = 'post'),
    path('<post_id>',read_post, name = 'readpost'),
    path('editpost/<post_id>',edit_post, name = 'editpost'),
    path('deletepost/<pk>',DeletePost.as_view(), name = 'deletepost'),
   
]