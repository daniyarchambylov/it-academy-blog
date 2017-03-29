from django.conf.urls import url
from blog.posts import views

urlpatterns = [
    url(r'^$', views.index, name='posts-index'),
    url(r'^details/(?P<id>\d+)/$', views.post_detail, name='posts-detail'),
    url(r'^draft/$', views.draft_posts, name='posts-draft'),
    url(r'^published/$', views.published_posts, name='posts-published'),
    url(r'^change-status/(?P<id>\d+)/$', views.change_status, name='posts-change-status'),
    url(r'^delete/(?P<id>\d+)/$', views.delete_post, name='post-delete'),
    url(r'^create-post/$', views.create_post, name='posts-create'),
    url(r'^update-post/(?P<post_id>\d+)/$', views.update_post, name='posts-update'),
    url(r'^create-post-form/$', views.create_post_with_forms, name='posts-create-form'),
    url(r'^create-post2/$', views.create_post_with_modelforms, name='posts-create-model-form'),
]
