from django.conf.urls import url,include
from . import views

urlpatterns = [
   url(r"^$", views.movie_list),

   url(r"^(?P<movie_id>\d+)/$", views.movie_songs),

   url(r"^new-movie/$", views.new_movie)
]