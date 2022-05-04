from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView

from accounts.views import *

urlpatterns = [
    path('subscribe/',subscribe, name = 'subscribe'),
    path('signup/',create_user, name = 'create_user'),
    path('login/',login_request, name = 'login'),
    path('logout/',LogoutView.as_view(template_name = 'accounts/logout.html'), name = 'logout'),
    path('updateuser/',update_user, name = 'update_user'),
    path('deleteteuser/<pk>',DeleteUser.as_view(), name = 'delete_user'),
    path('profile/',my_profile, name = 'my_profile'),
       
]