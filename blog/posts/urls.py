from django.conf.urls import url
from blog.posts import views

urlpatterns = [
    url(r'^$', views.index, name='posts-index'),
    url(r'^details/(?P<id>\d+)/$', views.post_detail, name='posts-detail'),
    url(r'^deleted/$', views.deleted_posts, name='posts-deleted'),
    url(r'^draft/$', views.draft_posts, name='posts-draft'),
    url(r'^published/$', views.published_posts, name='posts-published'),
    url(r'^change-status/(?P<id>\d+)/$', views.change_status, name='posts-change-status'),
    url(r'^delete/(?P<id>\d+)/$', views.delete_post, name='post-delete'),
]
