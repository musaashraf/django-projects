from my_app import models
from django import forms


class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = "__all__"


class AlbumForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.TextInput(attrs = {'type':'date'}))
    class Meta:
        model = models.Album
        fields = "__all__"
