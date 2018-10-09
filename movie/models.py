from django.db import models

class Movies(models.Model):
    movie_name=models.CharField(max_length=50)
    release_date=models.DateField()
    genre=models.CharField(max_length=25)
    poster=models.CharField(max_length=25)

    def __str__(self):
        return self.movie_name

class MovieSongs(models.Model):
    movie=models.ForeignKey(Movies,on_delete=models.CASCADE)
    song_name=models.CharField(max_length=100)
    song_type=models.CharField(max_length=10)
    song_img=models.CharField(max_length=50)
    song_length=models.CharField(max_length=10)

    def __str__(self):
        return self.song_name+"."+self.song_type