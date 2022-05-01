from django import forms
from django.contrib.auth.forms import UserCreationForm

class NewUserForm (UserCreationForm):
    first_name = forms.CharField(label='Name',required=False,max_length=40)
    last_name = forms.CharField(label='Last Name',required=False,max_length=60)
    email = forms.EmailField(label='Email',required=True,max_length=60)
    description = forms.CharField (label= 'Description',widget=forms.Textarea(attrs={'rows':5, 'cols':25}), required=False, max_length=400)
    web_page = forms.URLField (label= 'Web page', required=False)

class SubscriptionForm (forms.Form):
    name = forms.CharField(label='Name',required=False,max_length=40)
    last_name = forms.CharField(label='Last Name',required=False,max_length=60)
    email = forms.EmailField(label='Email',required=True,max_length=60)

class UserEditForm (forms.Form):
    username = forms.CharField (label = 'Username', max_length=150)
    first_name = forms.CharField (label = 'Name',max_length=150, required=False)
    last_name = forms.CharField (label = 'Last name',max_length=150, required=False)
    email = forms.EmailField (label= 'New email')
    description = forms.CharField (label= 'Description',widget=forms.Textarea(attrs={'rows':5, 'cols':25}), required=False, max_length=400)
    web_page = forms.URLField (label= 'Web page', required=False)
    password1 = forms.CharField (label= 'New password', widget=forms.PasswordInput)
    password2 = forms.CharField (label= 'Confirm new password', widget=forms.PasswordInput)

class UserWithAvatarEditForm (UserEditForm):
    image = forms.ImageField(label= 'Upload new profile picture')

class UserDisplayForm (forms.Form):
    username = forms.CharField (label = 'Username')
    first_name = forms.CharField (label = 'Name')
    last_name = forms.CharField (label = 'Last name')
    email = forms.EmailField (label= 'Email')
    description = forms.CharField (label= 'Description', widget=forms.Textarea(attrs={'rows':5, 'cols':25}))
