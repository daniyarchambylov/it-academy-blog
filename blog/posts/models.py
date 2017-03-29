from __future__ import unicode_literals

from django.db import models

from blog.authors.models import Author
from blog.categories.models import Category

STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
)


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=STATUS_CHOICES[0][0]
    )
    author = models.ForeignKey(Author, null=True, blank=True)
    categories = models.ManyToManyField(Category)

    def change_status(self):
        self.status = 'd' if self.status == 'p' else 'p'
        self.save()

