from app_users.models import Avatar
from app_messages.models import Message
from django.contrib.auth.models import User

# Auxiliary functions.

# Function that returns a user's profile image url
def get_avatar_url (user):
    try:
        avatar = Avatar.objects.filter (user_id = user.id)
        avatar_url = avatar[0].image.url
    except:
        avatar_url = ''

    return avatar_url



# Function that returns a form's errors if form.is_valid() = False
def get_errors (form):
    errors = []

    try:
        error_messages = form.errors.as_data().values()
        for error in error_messages:
            error_text = str(error[0]).replace("['","").replace("']","")
            errors.append(error_text)
    except:
        pass

    return errors

# Function that returns the active conversation of a user
def get_conversations (user):    
    messages_received = Message.objects.filter (receiver_id = user.id)
    messages_sent = Message.objects.filter(sender_id = user.id)
    message_list = messages_received.union(messages_sent) # messages in which the user engaged

    user_set = set()
    for message in message_list:
        if message.sender_id == user.id:
            other_user = User.objects.filter(id = message.receiver_id)[0]
        else:
            other_user = User.objects.filter(id = message.sender_id)[0]
       
        user_set.add(other_user) # other users with which the user has interacted

    # Generate conversations
    user_message_dict = {}
    user_avatar_dict = {}
    user_last_message_sender_dict = {}
    for user in user_set:
        user_messages_received = messages_sent.filter (receiver_id = user.id) # messages sent by request.user and received by user
        user_messages_sent = messages_received.filter(sender_id = user.id) # messages received by request.user and sent by user
        conversation_user = user_messages_received.union(user_messages_sent).order_by('id')
        last_message = list(conversation_user)[-1].message
        if len(last_message) > 15:
            last_message = last_message[0:15] + '...'
        else:
            last_message = last_message[0:15]
        user_avatar_url = get_avatar_url(user)
        user_message_dict [user] = last_message
        user_avatar_dict [user] = user_avatar_url

        # Getting last message's sender
        last_message_sender_id = list(conversation_user)[-1].sender_id
        try:
            sender = User.objects.get (id = last_message_sender_id)
            sender_username = sender.username
        except:
            sender_username = 'Sender not found'

        user_last_message_sender_dict [user] = sender_username 

    return user_message_dict, user_avatar_dict, user_last_message_sender_dict