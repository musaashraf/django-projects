from django.urls import path
from my_app import views
from .views import *

app_name = 'myapp'
urlpatterns = [
    path('', index, name="index"),
    path('add_album/', album_form, name='album_form'),
    path('add_musician/', musician_form, name='musician_form'),
    path('album_list/<int:artist_id>/', album_list, name='album_list'),
    path('edit_artist/<int:artist_id>/', edit_artist, name='edit_artist'),
    path('edit_album/<int:album_id>/', edit_album, name='edit_album'),
    path('delete_album/<int:album_id>/', delete_album, name='delete_album'),
]
