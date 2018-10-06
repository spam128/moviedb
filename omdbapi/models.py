from django.db import models


class Movie(models.Model):
    """Movie model, all fields are chars"""
    title = models.CharField(max_length=25, unique=True)
    year = models.CharField(max_length=10, default='N/A')
    rated = models.CharField(max_length=50, default='N/A')
    released = models.CharField(max_length=50, default='N/A')
    runtime = models.CharField(verbose_name='runtime in minutes', max_length=50, default='N/A')
    genre = models.CharField(max_length=100, default='N/A')
    director = models.CharField(max_length=100, default='N/A')
    writer = models.CharField(max_length=1000, default='N/A')
    actors = models.CharField(max_length=1000, default='N/A')
    plot = models.CharField(max_length=1000, default='N/A')
    language = models.CharField(max_length=50, default='N/A')
    country = models.CharField(max_length=300, default='N/A')
    awards = models.CharField(max_length=500, default='N/A')
    poster = models.CharField(default='N/A', max_length=200)
    metascore = models.CharField(max_length=50, default='N/A')
    imdbrating = models.CharField(max_length=10, verbose_name='imdb rating', default='N/A')
    imdbvotes = models.CharField(max_length=10, verbose_name='imdb votes', default='N/A')
    type = models.CharField(max_length=50, default='N/A')
    totalseasons = models.CharField(verbose_name='total seasons', default='N/A', max_length=10)

    def __str__(self):
        return getattr(self, 'title', '')


class Rating(models.Model):
    """Movie ratings from different websites"""
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    source = models.CharField(max_length=200, default='N/A')
    value = models.CharField(max_length=200, default='N/A')


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment = models.CharField(max_length=2048)
    date = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=20)
