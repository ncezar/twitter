from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Hashtag(models.Model):
        message = models.TextField()
        created_date=  models.DateTimeField(default=timezone.now)
        author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

        def publish(self):
            self.created_date = timezone.now()
            self.save()

        def __str__(self):
            return self.message
