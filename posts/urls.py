from django.conf.urls import url
from blog.posts import views

urlpatterns = [
    url(r'^$', views.index),
]
