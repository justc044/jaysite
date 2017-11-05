from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^invest/$', views.invest_list, name='invest_list'),
    url(r'^invest/new/$', views.invest_new, name='invest_new'),
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^blogs/$', views.blogs, name='blogs'),
    url(r'^blog/(?P<id>[0-9]+)/$', views.blog_list, name='blog_list'),
    url(r'^blog/remove/(?P<id>[0-9]+)/$', views.blog_remove, name='blog_remove'),
    url(r'^blog/edit/(?P<id>[0-9]+)/$', views.blog_edit, name='blog_edit'),
    url(r'^blog/new/$', views.blog_new, name='blog_new'),
    url(r'^goals/$', views.goals, name='goals'),
    url(r'^goal/new/$', views.goal_new, name='goal_new'),
]
