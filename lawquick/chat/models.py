from django.db import models
from user.models import User

# 채팅
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_title = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat by {self.user.email}"


# 메시지
class Message(models.Model):
    SENDER_CHOICES = (
        ('user', 'User'),
        ('bot', 'Bot'),
    )
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.CharField(max_length=10, choices=SENDER_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.sender} message at {self.created_at}"