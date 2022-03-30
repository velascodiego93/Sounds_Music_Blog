from django.shortcuts import render
from app_blog.forms import *
from app_blog.models import *
from datetime import datetime

# Create your views here.

def subscribe (request):
    if request.method == 'POST':
        new_subscription_form = SubscriptionForm (request.POST)
        
        if new_subscription_form.is_valid():
            data = new_subscription_form.cleaned_data
            new_subscription = Suscriptores(data['name'],
                                data['last_name'],
                                data['email'])

            new_subscription.save()

        return render (request, 'app_blog/index.html')  

    else:
        sub_form = SubscriptionForm()
        return render (request, 'app_blog/subscribe.html',{'subform': sub_form})    



def create_user (request):

    if request.method == 'POST':
        new_user_form = UserForm (request.POST)
        

        if new_user_form.is_valid():
            data = new_user_form.cleaned_data
            new_user = Usuario(data['name'],
                                data['last_name'],
                                data['username'],
                                data['email'],
                                data['occupation'],
                                data['workplace'])

            new_user.save()

        return render (request, 'app_blog/index.html')  

    else:
        user_form = UserForm()

    return render (request, 'app_blog/createuser.html',{'userform': user_form})    
    



def index (request):
    posts = Publicacion.objects.all()
    kw_form = KeywordForm()
    ctx = {'posts': posts, 'kw': kw_form}

    if request.GET != {}:
        bound_kw_form = KeywordForm(request.GET)
        
        if bound_kw_form.is_valid():
            data = bound_kw_form.cleaned_data
            posts = Publicacion.objects.filter (title__icontains = data['keyword'])
            ctx = {'posts': posts}
            return render (request, 'app_blog/searchpost.html', ctx)

    else:
        return render (request, 'app_blog/index.html', ctx)


def read_post (request, post_post):
    try: 
        post = Publicacion.objects.get(post = post_post)
        ctx = {'post': post}

        return render (request, 'app_blog/readpost.html', ctx)
    
    except:
        return render(request, 'app_blog/index.html')


def post (request):

    if request.method == 'POST':
        new_post_form = PubliForm (request.POST)
        
        if new_post_form.is_valid():
            data = new_post_form.cleaned_data
            new_post = Publicacion (data['title'],
                                    data['subtitle'],
                                    datetime.today(),
                                    data['author'],
                                    data['post'])

            new_post.save()

        return render (request, 'app_blog/index.html')  

    else:
        post_form = PubliForm()
        return render (request, 'app_blog/post.html',{'postform': post_form, 'date': datetime.today()})   

