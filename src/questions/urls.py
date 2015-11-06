from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^popular/$', views.popular, name='popular'),
    url(r'^ask/$', views.ask, name='ask'),
    url(r'^answers/$', views.answer, name='answer'),
    url(r'^$', views.index, name='index'),
]
