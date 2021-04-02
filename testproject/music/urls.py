from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^create$', views.AddRecord.as_view(), name='create'),
    # url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    url(r'^(?P<type>[0-9]+)/(?P<song_id>[0-9]+)/$', views.deleterecord.as_view(), name='deleterecord'),
]
