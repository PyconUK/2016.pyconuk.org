from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^news/$', views.news_items_view, name='news_items'),
    url(r'^news/(?P<datestamp>\d+)-(?P<key>[\w-]+)/$', views.news_item_view, name='news_item'),
    url(r'^$', views.page_view, name='index'),
    url(r'^(?P<key>.*?)/$', views.page_view, name='page'),
]
