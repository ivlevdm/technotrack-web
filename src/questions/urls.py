from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^popular/$', views.popular, name='popular'),
    url(r'^ask/$', views.ask, name='ask'),
    url(r'^answers/$', views.answer, name='answer'),
    url(r'search/', views.search, name='search'),
    url(r'tagsearch/', views.tag_search, name='tag_search'),
    url(r'^$', views.index, name='index'),
]
