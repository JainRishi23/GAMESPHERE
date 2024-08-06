# myApp/models.py
from django.db import models
from django.contrib.auth.models import User

class Feature(models.Model):
    name = models.CharField(max_length=100)

class Feature2(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=1000)
    
    def __str__(self):
        return f'{self.user.username} - {self.points} points'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    # Add additional fields here

    def __str__(self):
        return self.user.username


