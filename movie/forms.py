from django import forms
from . import models


class CreateMovieForm(forms.ModelForm):
    class Meta:
        model = models.Movies
        fields='__all__'
        # fields = ['movie_name', 'release_date', 'genre', 'poster']