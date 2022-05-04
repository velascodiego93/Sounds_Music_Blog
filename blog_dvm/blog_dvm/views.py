from re import U
from django.shortcuts import render, redirect
from pages.forms import *
from pages.models import *
from accounts.auxiliary import get_avatar_url

# Create your views here.

def home (request):
        return render (request, 'home.html')

def about_the_author (request):
    avatar_url = get_avatar_url (request.user)
    return render (request, 'about.html', {'avatar': avatar_url})
