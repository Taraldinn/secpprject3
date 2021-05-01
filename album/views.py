from django.shortcuts import render
from .models import Album
# Create your views here.


# photo album views

def album(request):
    album = Album.objects.all()
    context = {
        'album': album
    }

    return render(request, 'index.html', context)