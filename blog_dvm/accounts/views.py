from ast import excepthandler
from webbrowser import get
from django.db import IntegrityError
from django.forms import ValidationError
from django.shortcuts import redirect, render
from accounts.forms import *
from accounts.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.auxiliary import get_errors, get_avatar_url, get_conversations
from pages.models import Publicacion
from messages.models import Message


# Create your views here.

def subscribe (request):
    if request.method == 'POST':
        new_subscription_form = SubscriptionForm (request.POST)
        
        if new_subscription_form.is_valid():
            data = new_subscription_form.cleaned_data
            subscriptor = Suscriptores.objects.filter(email = data['email'])
            if len (subscriptor) == 0:
                new_subscription = Suscriptores(data['name'],
                                    data['last_name'],
                                    data['email'])
            
                new_subscription.save()
            
            else:
                errors = ['A subscription with that email already exists']
                new_subscription_form = SubscriptionForm (request.POST) 
                ctx = {'errors': errors, 'subform': new_subscription_form}
                return render (request, 'accounts/subscribe.html', ctx)

        else:
            errors = get_errors (new_subscription_form)
            new_subscription_form = SubscriptionForm (request.POST) 
            ctx = {'errors': errors, 'subform': new_subscription_form}
            return render (request, 'accounts/subscribe.html', ctx)

        return redirect ('index')

    else:
        sub_form = SubscriptionForm()
        return render (request, 'accounts/subscribe.html',{'subform': sub_form})

def create_user (request):

    if request.method == 'POST':
        user_creation_form = NewUserForm (request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()
            created_user = User.objects.get(username = request.POST['username'])
            
            created_user.first_name = request.POST['first_name']
            created_user.last_name = request.POST['last_name']
            created_user.email = request.POST['email']

            user_description = request.POST['description']
            user_web_page = request.POST['web_page']

            user_extra_information = UserExtraInformation (user = created_user, description = user_description, web_page = user_web_page)
            user_extra_information.save()

            created_user.save()
            return render (request, 'accounts/signup_success.html')

        else:
            errors = get_errors (user_creation_form)
            user_creation_form = NewUserForm (request.POST) 
            ctx = {'errors': errors, 'userform': user_creation_form}
            return render (request, 'accounts/signup.html', ctx)

    else:
        user_creation_form = NewUserForm ()
        return render (request, 'accounts/signup.html',{'userform': user_creation_form})
 

def login_request (request):

    if request.method == 'POST':
        user_login_form = AuthenticationForm (request, data = request.POST)

        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            username = data.get('username')
            password = data.get('password')

            user = authenticate(username = username, password = password)
            login (request, user)
            return redirect ('index')

        else:
            errors = get_errors (user_login_form)
            user_login_form = AuthenticationForm (request.POST) 
            ctx = {'errors': errors, 'userform': user_login_form}
            return render (request, 'accounts/login.html', ctx)

    else:
        user_login_form = AuthenticationForm ()
        return render (request, 'accounts/login.html',{'userform': user_login_form})


@login_required
def update_user (request):
    avatar_url = get_avatar_url (request.user)
    
    if request.method == 'POST':
        if request.user.is_superuser:
            user_edit_form = UserWithAvatarEditForm(request.POST, request.FILES)
        else:
            user_edit_form = UserEditForm(request.POST)

        if user_edit_form.is_valid():
            # Update profile information
            user = User.objects.get (id = request.user.id)
            user_data = user_edit_form.cleaned_data
                # Update User model information
            user.first_name = user_data.get('first_name')
            user.last_name = user_data.get('last_name')
            user.email = user_data.get('email')
            user.username = user_data.get('username')
                # Update UserExtraInformation model information
            user_description = user_data.get('description')
            user_web_page = user_data.get('web_page')

            try:
                user_extra_information = UserExtraInformation.objects.filter(user_id = request.user.id)[0]
                user_extra_information.description = user_description
                user_extra_information.web_page = user_web_page
                user_extra_information.save()
            except:
                user_extra_information = UserExtraInformation(user = request.user, description = user_description, web_page = user_web_page)
                user_extra_information.save()

            # Update profile image if the user is a superuser
            if request.user.is_superuser:
                user_avatar = Avatar.objects.filter(user_id = request.user.id)
                if len(user_avatar) > 0:
                    user_avatar = user_avatar[0]
                    user_avatar.image = request.FILES ['image']
                    user_avatar.save()
                else:
                    user_avatar = Avatar (user = request.user, image = request.FILES['image'])
                    user_avatar.save()

            # Update profile password
            if user_data.get('password1') != user_data.get('password2'):
                errors = ['Passwords are different. Please try again']
                if request.user.is_superuser:
                    user_edit_form = UserWithAvatarEditForm (request.POST, request.FILES)
                else:
                    user_edit_form = UserEditForm(request.POST)

                ctx = {'errors': errors, 'userform': user_edit_form, 'avatar': avatar_url}
                return render (request, 'accounts/updateuser.html', ctx)
            else:
                try:
                    validate_password (user_data.get('password1'),user=user)
                    user.set_password(user_data.get('password1'))
                    user.save()
                except Exception as exc:
                    print (exc)
                    if request.user.is_superuser:
                        user_edit_form = UserWithAvatarEditForm (request.POST, request.FILES)
                    else:                    
                        user_edit_form = UserEditForm (request.POST, request.FILES) 

                    if exc == ValidationError:
                        ctx = {'errors': exc, 'userform': user_edit_form, 'avatar': avatar_url}
                    else:
                        ctx = {'errors': ['A user with that username already exists'], 'userform': user_edit_form, 'avatar': avatar_url}
                        
                    return render (request, 'accounts/updateuser.html', ctx)
                    
            ctx = {'user': user, 'avatar': avatar_url}
            return render (request, 'accounts/updateuser_success.html', ctx)

        else:
            errors = get_errors (user_edit_form)
            user_edit_form = UserEditForm (request.POST, request.FILES) 
            ctx = {'errors': errors, 'userform': user_edit_form, 'avatar': avatar_url}
            return render (request, 'accounts/updateuser.html', ctx)

    else:
        dict_user = request.user.__class__.objects.filter(id = request.user.id).values().first()
        try:
            user_extra_information = UserExtraInformation.objects.filter(user_id = request.user.id)[0]
            dict_user['description'] = user_extra_information.description
            dict_user['web_page'] = user_extra_information.web_page
        except:
            dict_user['description'] = ''
            dict_user['web_page'] = ''
        
        if request.user.is_superuser:
            user_edit_form = UserWithAvatarEditForm (dict_user)
        else:
            user_edit_form = UserEditForm (dict_user)

        ctx = {'userform': user_edit_form, 'avatar': avatar_url}
        return render (request, 'accounts/updateuser.html', ctx)



@login_required
def my_profile (request):
    
    # Display user's data
    avatar_url = get_avatar_url (request.user)
    dict_user = request.user.__class__.objects.filter(id = request.user.id).values().first()
    try: 
        user_extra_information = UserExtraInformation.objects.filter(user_id = request.user.id)[0]
        dict_user['description'] = user_extra_information.description
        dict_user['web_page'] = user_extra_information.web_page
    except:
        dict_user['description'] = ''
        dict_user['web_page'] = ''
    
    user_display_form = UserDisplayForm (dict_user)

    # Display user's posts
    posts = Publicacion.objects.filter (author = request.user.username).order_by('-date_of_publication')

    # Display user's active conversations
    conversation_data = get_conversations(request.user)
    user_message_dict = conversation_data[0]
    user_avatar_dict = conversation_data[1]
    user_last_message_sender_dict = conversation_data[2]
       
    ctx = {'userform': user_display_form, 'avatar': avatar_url, 'user_posts': posts, 'user_message_dict': user_message_dict, 'user_avatar_dict': user_avatar_dict, 'user_last_message_sender_dict': user_last_message_sender_dict, 'web_page': dict_user['web_page']}
    return render (request, 'accounts/profile.html', ctx)


class DeleteUser (LoginRequiredMixin, DeleteView):
    model = User
    success_url = '../../../pages/index'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        avatar_url = get_avatar_url (self.request.user)
        context['avatar'] = avatar_url

        return context
