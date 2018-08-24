from rest_framework import serializers
from .models import Movie, Comment, Rating
from moviesrestapi import omdbapi


class MovieSerializer(serializers.ModelSerializer):
    """serializes data from omdbapi.
    TODO: serialize Ratings
    """

    def to_internal_value(self, data):
        movie_data = omdbapi.save(data.get('title'))
        movie_data2 = SaveMovieSerializer(data=movie_data)
        if movie_data.get('response') == 'False':
            raise serializers.ValidationError(movie_data)
        if not movie_data2.is_valid():
            raise serializers.ValidationError(movie_data2.errors)
        return movie_data2.data

    class Meta:
        model = Movie
        read_only_fields = (
            'year', 'rated', 'released', 'runtime', 'genre', 'director', 'writer', 'actors', 'plot', 'language',
            'country', 'awards', 'poster', 'metascore', 'imdbrating', 'imdbvotes', 'type', 'totalseasons')
        exclude = ('id',)


class SaveMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
