from django.db import models
from django.contrib.auth.models import User
import time

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_picture = models.FileField(upload_to='static/profile_pic'+str(time.time()), default='avi.jpg')
    address = models.TextField(max_length=300)
    city = models.TextField(max_length=300)
    contact = models.BigIntegerField()

    def __str__(self):
        return self.user.username
