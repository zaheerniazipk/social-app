from django.db import models
from django.contrib.auth.models import User  # For creating User


# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=240)
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    # return post text instead of post object
    def __str__(self):
        return self.text[0:100]
