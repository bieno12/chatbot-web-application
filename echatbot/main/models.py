from django.db import models

# Create your models here.

class Conversation(models.Model):
	id = models.AutoField(primary_key=True)
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=255, default="Unnamed Conversation")
class Message(models.Model):
	id = models.AutoField(primary_key=True)
	sender = models.CharField(
        max_length=10,
        choices=[("bot", "Bot"), ("user", "User")],
        default="user",
    )
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	conversation = models.ForeignKey(
        "Conversation",
        on_delete=models.CASCADE,
    )
