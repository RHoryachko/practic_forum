# music/urls.py
from django.urls import path
from .views import upload_music, list_music

urlpatterns = [
    path('upload/', upload_music, name='upload_music'),
    path('', list_music, name='music_list'),
]
