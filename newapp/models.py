from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _ 
from django.utils.timezone import now

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), max_length=254,unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email



class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(editable=False)
    modified_at =models.DateTimeField(auto_now=True)

    def save(self):
        if not self.id:
            self.created_at = now()
        return super().save()

    
    def __str__(self):
        return self.title


    