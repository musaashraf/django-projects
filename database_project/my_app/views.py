from django.shortcuts import render
from django.http import HttpResponse
from my_app import forms
from my_app.models import Musician, Album
from django.db.models import Avg
from django.template.response import TemplateResponse


def index(request):
    # musician_list = Musician.objects.all()
    musician_list = Musician.objects.order_by('first_name')

    diction = {'title': "Home Page", 'musician_list': musician_list}
    return render(request, 'myapp/index.html', context=diction)


def album_list(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    album = Album.objects.filter(artist=artist_id).order_by('name', 'release_date')
    artist_rating = Album.objects.filter(artist=artist_id).aggregate(Avg('num_stars'))

    diction = {'title': "List of Albums", 'artist_info': artist_info, 'album_list': album,
               'artist_rating': artist_rating}
    return render(request, 'myapp/album_list.html', context=diction)


def musician_form(request):
    form = forms.MusicianForm()
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    diction = {'title': "Add Musician", 'musician_form': form}
    return render(request, 'myapp/musician_form.html', context=diction)


def album_form(request):
    form = forms.AlbumForm()
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {'title': "Add Album", 'album_form': form}
    return render(request, 'myapp/album_form.html', context=diction)


def edit_artist(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    form = forms.MusicianForm(instance=artist_info)
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST, instance=artist_info)

        if form.is_valid():
            form.save(commit=True)
            return album_list(request, artist_id)
    diction = {'edit_form': form}
    return render(request, 'myapp/edit_artist.html', context=diction)


def edit_album(request, album_id):
    album_info = Album.objects.get(pk=album_id)
    form = forms.AlbumForm(instance=album_info)
    diction={}
    if request.method == 'post':
        form = forms.AlbumForm(request.post, instance=album_info)
        if form.is_valid():
            form.save(commit=True)
            diction.update({'success_text': 'Successfully Updated!'})

    diction = {'edit_album': form}
    diction.update({'album_id': album_id})
    return render(request, 'myapp/edit_album.html', context=diction)

def delete_album(request, album_id):
    album = Album.objects.get(pk=album_id).delete()
    diction = {'delete_success': 'Album deleted Successfully! '}
    return render(request, 'myapp/delete.html', context=diction)