from .models import Movie, Comment
from .serializers import MoviesSerializer, CommentSerializer, CreateMovieSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import viewsets


class MoviesViewSet(viewsets.ModelViewSet):
    """Viewset for adding movies and retrieving"""
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer
    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ('title', 'year')
    ordering = ('title',)

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateMovieSerializer
        else:
            return MoviesSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    """Viewset for adding comments and retrieving"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ('user_name',)
    ordering_fields = ('date', 'user_name', 'movie')
    ordering = ('date',)
