from django.shortcuts import render
import requests
from .models import Movie, Comment
from django.views.decorators.csrf import csrf_exempt
from django.template.defaultfilters import slugify
from rest_framework.decorators import api_view
import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import MovieSerializer, RatingSerializer, CommentSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets


@api_view(['POST', ])
def movies_view(request, pk='', format=None):
    if request.method == 'POST':
        name = slugify(request.data['title']).replace('-', '+')
        resp = requests.get('http://www.omdbapi.com/?apikey=7b85cd2d&t={}'.format(name))
        data = json.loads(resp.content)
        data = {key.lower(): data[key] for key in data}
        data['imdbvotes'] = int(data['imdbvotes'].replace(',', ''))
        movie = MovieSerializer(data=data)
        if movie.is_valid():
            movie.save()
        else:
            return Response(movie.errors, status=status.HTTP_400_BAD_REQUEST)
        for rating in data['ratings']:
            rating['movie'] = movie.instance.id
        ratings = RatingSerializer(data=data['ratings'], many=True)
        if ratings.is_valid():
            ratings.save()
            return Response(movie.data, status=status.HTTP_201_CREATED)
        return Response(ratings.errors, status=status.HTTP_400_BAD_REQUEST)


class MoviesViewSet(generics.ListCreateAPIView, viewsets.GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    # filter_fields = ('date', 'user_name', 'date')
    # ordering_fields = ('date', 'user_name', 'movie')
    ordering = ('title',)
    def create(self, request,*args, **kwargs):
        try:
            name = slugify(request.data['title']).replace('-', '+')
            resp = requests.get('http://www.omdbapi.com/?apikey=7b85cd2d&t={}'.format(name))
            data = json.loads(resp.content)
            data = {key.lower(): data[key] for key in data}
            data['imdbvotes'] = int(data['imdbvotes'].replace(',', ''))
            movie = MovieSerializer(data=data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        if movie.is_valid():
            movie.save()
        else:
            return Response(movie.errors, status=status.HTTP_400_BAD_REQUEST)
        for rating in data['ratings']:
            rating['movie'] = movie.instance.id
        ratings = RatingSerializer(data=data['ratings'], many=True)
        if ratings.is_valid():
            ratings.save()
            return Response(movie.data, status=status.HTTP_201_CREATED)
        return Response(ratings.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentsLC(generics.ListCreateAPIView, viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    filter_fields = ('date', 'user_name', 'date')
    ordering_fields = ('date', 'user_name', 'movie')
    ordering = ('date',)
