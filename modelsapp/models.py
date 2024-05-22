from django.db import models
from django.contrib.auth.models import User
import time

from django.dispatch import receiver
from django.db.models.signals import post_save

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_picture = models.FileField(upload_to='static/profile_pic'+str(time.time()), default='20240311_081940.jpg')
    address = models.TextField(max_length=300, default='P.O BOX 140')
    city = models.TextField(max_length=300, default='Nairobi')
    contact = models.BigIntegerField(null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfileInfo.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofileinfo.save()