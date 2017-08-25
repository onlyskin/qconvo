from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/users/([\w\d]+)/([\w\d]+)$', views.users, name='users'),
    url(r'^api/languages/$', views.languages, name='languages'),
]
