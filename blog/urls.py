from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^authors/', include('blog.authors.urls')),
    url(r'^categories/', include('blog.categories.urls')),
    url(r'^test/messages/$', views.test_messages),
    url(r'^', include('blog.posts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
