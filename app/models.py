from django.db import models

# Create your models here.
class Message(models.Model):
    chat_id = models.IntegerField()
    type = models.CharField(max_length=10)
    text = models.TextField()
