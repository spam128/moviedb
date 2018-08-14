import requests
from .models import Movie, Comment
from django.template.defaultfilters import slugify
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import MovieSerializer, RatingSerializer, CommentSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import viewsets


class MoviesViewSet(generics.ListCreateAPIView, viewsets.GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ('title', 'year')
    ordering = ('title',)

    def create(self, request, *args, **kwargs):
        try:
            name = slugify(request.data['title']).replace('-', '+')
            resp = requests.get('http://www.omdbapi.com/?apikey=7b85cd2d&t={}'.format(name))
            data = resp.json()
            data = {key.lower(): data[key] for key in data}
            data['imdbvotes'] = float(data.get('imdbvotes', '0').replace(',', ''))
            data['imdbrating'] = float(data.get('imdbrating', '0').replace(',', ''))
            movie = MovieSerializer(data=data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        if movie.is_valid():
            movie.save()
        else:
            return Response(movie.errors, status=status.HTTP_400_BAD_REQUEST)

        data['ratings'] = data.get('ratings', {})
        for rating in data['ratings']:
            rating['movie'] = movie.instance.id
        ratings = RatingSerializer(data=data['ratings'], many=True)
        if ratings.is_valid():
            ratings.save()
        return Response(movie.data, status=status.HTTP_201_CREATED)


class CommentsLC(generics.ListCreateAPIView, viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ('user_name',)
    ordering_fields = ('date', 'user_name', 'movie')
    ordering = ('date',)
