from django import forms
from django_summernote.widgets import SummernoteWidget

class PubliForm (forms.Form):
    title = forms.CharField(required=True,max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    subtitle = forms.CharField(required=True,max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Subtitle'}))
    post = forms.CharField(widget=SummernoteWidget(),required=True, max_length=15000)
    image = forms.ImageField(label= 'Choose post cover picture:')


class KeywordForm (forms.Form):
    keyword = forms.CharField()


