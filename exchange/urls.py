from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/profiles$', views.profiles, name='profiles'),
    url(r'^api/languages/$', views.languages, name='languages'),
]
