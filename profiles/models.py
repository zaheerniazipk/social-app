from django.contrib.auth.models import User  # For creating new user
from django.db import models

# Django signals
from django.db.models.signals import post_save
from django.dispatch import receiver

# sorl-thumbnail
from sorl.thumbnail import ImageField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    image = models.ImageField(upload_to='profiles')

    # render username instead of objects
    def __str__(self):
        return self.user.username


# Django Signals
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """ Create a new Profile() object when a new Django user is created! """
    if created:
        Profile.objects.create(user=instance)
