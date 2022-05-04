from unittest.util import safe_repr
from django.db import models
from django import utils
from django.contrib.auth.models import User

# Create your models here.

class Message (models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField (default=utils.timezone.now)
    sender = models.ForeignKey (User, on_delete=models.CASCADE, related_name='+')
    receiver = models.ForeignKey (User, on_delete=models.CASCADE, related_name='+')
    message = models.CharField (max_length=15000)

    def __str__(self):
        sender = User.objects.filter(id = self.sender_id)[0].username
        receiver = User.objects.filter(id = self.receiver_id)[0].username

        return f'{self.id} - from {sender} to {receiver}: {self.message}'





