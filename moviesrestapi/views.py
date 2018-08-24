from .models import Movie, Comment
from rest_framework import generics
from .serializers import MovieSerializer, CommentSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import viewsets


class MoviesViewSet(generics.ListCreateAPIView, viewsets.GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ('title', 'year')
    ordering = ('title',)
    # data['ratings'] = data.get('ratings', {})
    # for rating in data['ratings']:
    #     rating['movie'] = movie.instance.id
    # ratings = RatingSerializer(data=data['ratings'], many=True)
    # if ratings.is_valid():
    #     ratings.save()
    # return Response(movie.data, status=status.HTTP_201_CREATED)


class CommentsLC(generics.ListCreateAPIView, viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ('user_name',)
    ordering_fields = ('date', 'user_name', 'movie')
    ordering = ('date',)
