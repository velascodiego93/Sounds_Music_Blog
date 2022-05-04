from django.contrib import admin
from django.urls import path

from messages.views import *

urlpatterns = [
    path('conversation/<receiver_id>',conversation, name = 'conversation'),
    path('new_conversation/',new_conversation, name = 'new_conversation'),
   
]