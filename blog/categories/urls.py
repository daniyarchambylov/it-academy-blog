from blog.categories import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.list_categories, name='categories-list'),
]