from django.conf.urls import url
from django.views.generic.base import TemplateView

from blog.cbv.views import CustomTemplateView, CustomTemplateView2, PostCBV

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='cbv/first_view.html')),
    url(r'^second/$', CustomTemplateView.as_view()),
    url(r'^third/$', CustomTemplateView2.as_view()),
    url(r'^posts/$', PostCBV.as_view()),
]