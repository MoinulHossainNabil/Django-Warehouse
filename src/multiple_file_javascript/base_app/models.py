from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=40, blank=True)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class MultipleFieldJavascript(models.Model):
    data = models.CharField(max_length=30)

    def __str__(self):
        return self.data
