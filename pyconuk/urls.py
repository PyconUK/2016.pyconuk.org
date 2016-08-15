from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^schedule/$', views.schedule_view, name='schedule'),
    url(r'^open-day/$', views.open_day_view, name='open_day'),
    url(r'^news/$', views.news_items_view, name='news_items'),
    url(r'^news/(?P<datestamp>\d+)-(?P<key>[\w-]+)/$', views.news_item_view, name='news_item'),
    url(r'^(?P<session_type>talks|workshops)/(?P<slug>[\w-]+)/$', views.session_view, name='session'),
    url(r'^speakers/(?P<key>[\w-]+)/$', views.speaker_view, name='speaker'),
    url(r'^sponsors/(?P<key>[\w-]+)/$', views.sponsor_view, name='sponsor'),
    url(r'^$', views.page_view, name='index'),
    url(r'^(?P<key>.*?)/$', views.page_view, name='page'),
]
