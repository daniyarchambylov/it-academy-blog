from __future__ import unicode_literals

from django.conf import settings
from django.db import models

GENDER_CHOICES = (
    ('m', 'Male'),
    ('f', 'Female'),
)


class Author(models.Model):
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to='authors', blank=True, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True, null=True)

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __unicode__(self):
        return self.get_full_name()
