from django import forms

class UserForm (forms.Form):
    name = forms.CharField(label='Name',required=False,max_length=40)
    last_name = forms.CharField(label='Last Name',required=False,max_length=60)
    username = forms.CharField(label='Username',required=True,max_length=40)
    email = forms.EmailField(label='Email',required=True,max_length=60)
    occupation = forms.CharField(label='Occupation',required=False,max_length=40)
    workplace = forms.CharField(label='Workplace',required=False,max_length=40)


class PubliForm (forms.Form):
    title = forms.CharField(required=True,max_length=50)
    subtitle = forms.CharField(widget=forms.Textarea,required=False,max_length=100)
    author = forms.CharField(max_length=40, required=True)
    post = forms.CharField(widget=forms.Textarea,required=True,max_length=2500)
    heading = forms.CharField(max_length=60,required=False)


class KeywordForm (forms.Form):
    keyword = forms.CharField()

class SubscriptionForm (forms.Form):
    name = forms.CharField(label='Name',required=False,max_length=40)
    last_name = forms.CharField(label='Last Name',required=False,max_length=60)
    email = forms.EmailField(label='Email',required=True,max_length=60)
