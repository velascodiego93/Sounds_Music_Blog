from re import U
from django.shortcuts import render, redirect
from pages.forms import *
from pages.models import *
from accounts.models import Avatar
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.auxiliary import get_avatar_url, get_errors
from django.views.generic.edit import DeleteView, UpdateView

# Create your views here.

def index (request):
    posts = Publicacion.objects.order_by('-date_of_publication')
    kw_form = KeywordForm()

    avatar_url = get_avatar_url (request.user)

    if request.GET != {}:
        bound_kw_form = KeywordForm(request.GET)
        
        if bound_kw_form.is_valid():
            data = bound_kw_form.cleaned_data
            posts = Publicacion.objects.filter (title__icontains = data['keyword']).order_by('-date_of_publication')
            ctx = {'posts': posts, 'avatar': avatar_url}
            return render (request, 'pages/searchpost.html', ctx)
        else:
            errors = get_errors(bound_kw_form)
            ctx = {'errors': errors, 'kw': bound_kw_form, 'avatar': avatar_url}
            return render (request, 'pages/index.html', ctx)           

    else:
        ctx = {'posts': posts, 'kw': kw_form, 'avatar': avatar_url}
        return render (request, 'pages/index.html', ctx)


def read_post (request, post_id):
    avatar_url = get_avatar_url (request.user)
    try: 
        post = Publicacion.objects.get(id = post_id)
        ctx = {'post': post, 'avatar': avatar_url}

        return render (request, 'pages/readpost.html', ctx)
    
    except:
        return redirect ('index')


@login_required
def post (request):
    avatar_url = get_avatar_url (request.user)
    if request.method == 'POST':
        new_post_form = PubliForm (request.POST, request.FILES)
        
        if new_post_form.is_valid():
            data = new_post_form.cleaned_data
            new_post = Publicacion (title = data['title'],
                                    subtitle = data['subtitle'],
                                    date_of_publication = datetime.now(),
                                    author = request.user.username,
                                    post = data['post'],
                                    image = request.FILES ['image']
                                    )

            new_post.save()
        else:
            errors = get_errors(new_post_form)
            new_post_form = PubliForm (request.POST, request.FILES) 
            ctx = {'errors': errors, 'postform': new_post_form, 'date': datetime.now()}
            return render (request, 'pages/post.html', ctx)

        return redirect ('index')  

    else:
        post_form = PubliForm()
        ctx = {'postform': post_form, 'date': datetime.now(), 'avatar': avatar_url}
        return render (request, 'pages/post.html', ctx)   


class DeletePost (LoginRequiredMixin, DeleteView):
    model = Publicacion
    success_url = '../../accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        avatar_url = get_avatar_url (self.request.user)
        context['avatar'] = avatar_url

        return context


@login_required
def edit_post (request, post_id):
    avatar_url = get_avatar_url (request.user)
    post_to_edit = Publicacion.objects.get (id = post_id)
    post_to_edit_dict = post_to_edit.__dict__
    bound_edit_form = PubliForm (post_to_edit_dict)
    previous_cover = post_to_edit.image.url


    if request.method == 'POST':
        new_bound_edit_form = PubliForm (request.POST, request.FILES)
        
        if new_bound_edit_form.is_valid():
            data = new_bound_edit_form.cleaned_data

            post_to_edit.title = data['title']
            post_to_edit.subtitle = data['subtitle']
            post_to_edit.post = data['post']
            post_to_edit.date_of_publication = datetime.now()
            post_to_edit.image = request.FILES['image']

            post_to_edit.save()
        else:
            errors = get_errors(new_bound_edit_form)
            bound_edit_form = PubliForm (request.POST, request.FILES) 
            ctx = {'errors': errors, 'form': bound_edit_form, 'date': datetime.now()}
            return render (request, 'pages/editpost.html', ctx)

        return redirect ('my_profile') 

    else:
        ctx = {'form': bound_edit_form, 'date': datetime.now(), 'avatar': avatar_url, 'previous_cover': previous_cover}
        return render (request, 'pages/editpost.html', ctx)   


