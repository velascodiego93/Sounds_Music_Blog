from django.shortcuts import render, redirect
from messages.models import Message
from accounts.auxiliary import get_avatar_url, get_errors, get_conversations
from messages.forms import *
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required
def conversation (request, receiver_id):
    receiver = User.objects.get(id = receiver_id)
    messages_sent = Message.objects.filter (sender_id = request.user.id).filter(receiver_id = receiver.id)
    messages_received = Message.objects.filter (sender_id = receiver.id).filter(receiver_id = request.user.id)
    conversation = messages_sent.union(messages_received).order_by ('date')

    message_form = MessageForm()

    avatar_sender_url = get_avatar_url (request.user)
    avatar_receiver_url = get_avatar_url (receiver)

    if request.method == 'POST':
        bound_message_form = MessageForm(request.POST)
        
        if bound_message_form.is_valid():
            data = bound_message_form.cleaned_data
            message = Message (date = datetime.now(),
                                sender = request.user,
                                receiver = receiver,           
                                message = data['message'])
            message.save()

            ctx = {'conversation': conversation, 'avatar': avatar_sender_url, 'avatar_receiver': avatar_receiver_url, 'receiver': receiver, 'form': message_form}
            return render (request, 'messages/conversation.html', ctx)
        else:
            errors = get_errors(bound_message_form)
            ctx = {'conversation': conversation,'errors': errors, 'avatar': avatar_sender_url, 'avatar_receiver': avatar_receiver_url, 'receiver': receiver, 'form': message_form}
            return render (request, 'messages/conversation.html', ctx)           

    else:
        ctx = {'conversation': conversation, 'avatar': avatar_sender_url, 'avatar_receiver': avatar_receiver_url, 'receiver': receiver, 'form': message_form}
        return render (request, 'messages/conversation.html', ctx)


@login_required
def new_conversation (request):

    # Display user's active conversations
    conversation_data = get_conversations(request.user)
    user_message_dict = conversation_data[0]
    user_avatar_dict = conversation_data[1]
    user_last_message_sender_dict = conversation_data[2]

    message_form = MessageFormWithReceiver()
    avatar_sender_url = get_avatar_url (request.user)
    
    if request.method == 'POST':
        bound_message_form = MessageFormWithReceiver(request.POST)
        
        if bound_message_form.is_valid():
            data = bound_message_form.cleaned_data
            message = Message (date = datetime.now(),
                                sender = request.user,
                                receiver = data['receiver'],           
                                message = data['message'])
            message.save()
            receiver = data['receiver']
        
            return redirect ('conversation', receiver_id = receiver.id)
        else:
            errors = get_errors (bound_message_form)
            ctx = {'avatar': avatar_sender_url, 'form': bound_message_form, 'errors': errors, 'user_message_dict': user_message_dict, 'user_avatar_dict': user_avatar_dict, 'user_last_message_sender_dict': user_last_message_sender_dict}
            return render (request, 'messages/new_conversation.html', ctx)

    else:
        ctx = {'avatar': avatar_sender_url, 'form': message_form, 'user_message_dict': user_message_dict, 'user_avatar_dict': user_avatar_dict, 'user_last_message_sender_dict': user_last_message_sender_dict}
        return render (request, 'messages/new_conversation.html', ctx)


            

