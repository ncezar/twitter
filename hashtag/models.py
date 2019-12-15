from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Hashtag(models.Model):
        message = models.TextField()

        def publish(self):
            self.created_date = timezone.now()
            self.save()

        def __str__(self):
            return self.message

class Tweet(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.CharField(max_length=160)
    created_at = models.DateTimeField(auto_now_add=True)
