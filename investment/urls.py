from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^invest/$', views.invest_list, name='invest_list'),
    url(r'^invest/new/$', views.invest_new, name='invest_new'),
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^blogs/$', views.blogs, name='blogs'),
    url(r'^blog/(?P<id>[0-9]+)/$', views.blog_list, name='blog_list'),
    url(r'^blog/new/$', views.blog_new, name='blog_new'),
]
