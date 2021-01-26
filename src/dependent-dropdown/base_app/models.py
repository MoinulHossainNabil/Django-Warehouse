from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=40, blank=True)
    age = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey('Country', null=True, on_delete=models.SET_NULL, related_name='user_country')
    city = models.ForeignKey('City', null=True, on_delete=models.SET_NULL, related_name='user_city')

    def __str__(self):
        return self.user.username


class Country(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=60)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey('Country', null=True, on_delete=models.SET_NULL, related_name='person_country')
    city = models.ForeignKey('City', null=True, on_delete=models.SET_NULL, related_name='person_city')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('base_app:person-list')



    
