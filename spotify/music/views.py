from django.shortcuts import render
from .models import Album, Song



def Home(request):
    albums = Album.objects.all()
    songs = Song.objects.all()
    context = {
        "albums": albums,
        "songs": songs
    }
    return render(request, 'music/home.html',context)
