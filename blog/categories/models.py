from __future__ import unicode_literals

from django.db import models

from blog.posts.models import Post


class Category(models.Model):
    name = models.CharField(max_length=30)
    posts = models.ManyToManyField(Post)

    def __unicode__(self):
        return self.name
