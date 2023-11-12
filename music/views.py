# music/views.py
from django.shortcuts import render, redirect
from .models import Song
from .forms import SongForm



def upload_music(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_music')
    else:
        form = SongForm()
    return render(request, 'music/upload_music.html', {'form': form})

def list_music(request):
    songs = Song.objects.all()
    return render(request, 'music/list_music.html', {'songs': songs})
