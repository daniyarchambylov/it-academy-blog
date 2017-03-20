from django.conf.urls import url

from blog.authors import views

urlpatterns = [
    url(r'^$', views.authors_list, name='authors-list'),
    url(r'^add/$', views.authors_add, name='authors-add'),
    url(r'^(?P<author_id>\d+)/edit-email/$', views.author_edit_email, name='authors-edit-email'),
]