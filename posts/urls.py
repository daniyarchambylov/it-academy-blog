from django.conf.urls import url
from blog.posts import views

urlpatterns = [
    url(r'^$', views.index, name='posts-index'),
    url(r'^details/$', views.post_detail, name='posts-detail'),
    url(r'^deleted/$', views.deleted_posts, name='posts-deleted'),
]
