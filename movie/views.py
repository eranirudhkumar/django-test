from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms
from .models import Movies,MovieSongs
from django.contrib import messages

# import sys
# import os

# os.chdir("../")

# sys.append("../")

# from blog import view

def movie_list(request):
    all_movie=Movies.objects.all()
    context={
        "all_movie":all_movie,
        "img_1":"img/Inspirational.jpg"
    }
    return render(request, "movie/index.html",context)


def movie_songs(request,movie_id):
    movie_songs=MovieSongs.objects.filter(movie_id=movie_id)

    if not len(movie_songs):
        messages.info(request,"Songs not Found.")
    context={
        "movie_songs":movie_songs
    }

    # return HttpResponse("<h1>Your Movies id is "+str(movie_id)+"</h1>")
    # return HttpResponse("<h1>Your Movies id is {} </h1>".format(movie_id))
    return render(request,"movie/songs/movie_songs.html",
                  context)


def new_movie(request):
    movie_form=forms.CreateMovieForm()

    if request.method=='POST':
        movie_form = forms.CreateMovieForm(request.POST)
        if movie_form.is_valid():
            moviename=movie_form.cleaned_data.get("movie_name")
            moviereleasedate=movie_form.cleaned_data.get("release_date")
            moviegenre=movie_form.cleaned_data.get("genre")
            movieposter=movie_form.cleaned_data.get("poster")

            movie_object=Movies(movie_name=moviename,
                                release_date=moviereleasedate,
                                genre=moviegenre,
                                poster=movieposter)
            movie_object.save()

            # print(moviename)
            # print(moviereleasedate)
            # print(moviegenre)
            # print(movieposter)
            messages.info(request,"Data saved.")
            # messages.error(request,"Something went wrong.")
            # messages.warning(request,"Data missing, Data saved.")
            return redirect("/movies/")
    context={
        'movie_form':movie_form
    }
    return render(request,'movie/new_movies.html',
                  context)