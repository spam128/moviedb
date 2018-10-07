from omdbapi.urls import router as omdb
from imdbapi.urls import router as imdb
from django.urls import include, path

urlpatterns = [
    path(r'omdb/', include((omdb.urls, 'omdbapi'))),
    path(r'imdb/', include((imdb.urls, 'imdbapi'))),

]
