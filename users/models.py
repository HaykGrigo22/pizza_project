from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

from helpers.storage import upload_user_image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_user_image, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}"


@receiver(post_save, sender=User)
def post_save_user(instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

