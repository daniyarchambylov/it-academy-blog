from __future__ import unicode_literals

from django.db import models

GENDER_CHOICES = (
    ('m', 'Male'),
    ('f', 'Female'),
)


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(auto_now=True)

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)