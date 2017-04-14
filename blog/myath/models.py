# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone


class MyUserManager(models.Manager):
    def _create_user(self, phone, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not phone:
            raise ValueError('The given username must be set')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)

    def get_by_natural_key(self, username):

        '''
        Example: objects = MyUserManager()
                 objects.get_by_natural_key('555000111')
        Explanation:
          The same as MyUser.objects.get()
          1. **{ 'phone': '5550001111' }
          2. phone='555000111
          3. self.get(phone='555000111')
          4. MyUser.objects.get(phone='555000111')
        '''

        return self.get(**{self.model.USERNAME_FIELD: username})


class MyUser(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=9, unique=True)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    email = models.CharField(max_length=100, blank=True)

    USERNAME_FIELD = 'phone'

    object = MyUserManager()

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name