from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from django.contrib.auth import get_user_model

from .models import Author

User = get_user_model()

# class InlineUser(InlineModelAdmin):
#     model = User

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender')
    list_filter = ['gender']
    # inlines = (InlineUser,)

admin.site.register(Author, AuthorAdmin)
