from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _ 


class CustomUserManager(BaseUserManager):

    def create_user(self,email,password,**extra_key):
        if not email:
            raise ValueError(_('Email is Required'))
        email = self.normalize_email(email)
        user = self.model(email=email , **extra_key)
        user.set_password(password)
        user.save()
        return user

    
    def create_superuser(self,email,password,**extra_key):

        extra_key.setdefault('is_staff' , True)
        extra_key.setdefault('is_superuser' , True)
        extra_key.setdefault('is_active' , True)

        if not extra_key.get('is_staff') is True:
            raise ValueError(_('is staff should be True'))
        if not extra_key.get('is_superuser') is True:
            raise ValueError(_('is superuser should be True'))
        self.create_user(email,password,**extra_key)

