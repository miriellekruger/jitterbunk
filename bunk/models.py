from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User as AuthUser

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    photo = models.URLField(max_length=200)
    auth_user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

class Bunk(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bunks_sent")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bunks_received")
    time = models.DateTimeField("time bunked", default=timezone.now)




