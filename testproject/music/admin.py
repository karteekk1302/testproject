from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Song,Podcast,Audiobook

admin.site.register(Podcast)
admin.site.register(Audiobook)
admin.site.register(Song)
