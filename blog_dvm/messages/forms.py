from django import forms
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget
from messages.models import Message

class MessageForm (ModelForm):
    class Meta:
        model = Message
        fields = ['message']
        widgets = {'message': SummernoteWidget()}



class MessageFormWithReceiver (ModelForm):
    class Meta:
        model = Message
        fields = ['receiver','message']
        widgets = {'message': SummernoteWidget()}