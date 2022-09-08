from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Follower(models.Model):
    followed_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followed_by',
    )

    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
    )

    #  # return user
    def __str__(self):
        return f"{self.followed_by.id} is following {self.following.id}"

    # uniqueness | one follower can follow other user only once
    class Meta:
        unique_together = ('followed_by', 'following',)
