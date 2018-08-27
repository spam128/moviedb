from rest_framework import serializers
from .models import Movie, Comment, Rating
from moviesrestapi import omdbapi


class CreateMovieSerializer(serializers.ModelSerializer):
    """serializer for saving movie to database given only movie title."""

    class Meta:
        model = Movie
        fields = ('title',)

    def create(self, data):
        """save to database movie info from omdbapi."""
        movie_data = omdbapi.get_movie(data.get('title', ''))
        movie_serializer = MoviesSerializer(data=movie_data)
        if movie_data.get('response') == 'False':
            raise serializers.ValidationError(movie_data)
        movie_serializer.is_valid(raise_exception=True)
        movie_serializer.save()
        print('exit')
        return movie_serializer.data


class RatingSerializer(serializers.ModelSerializer):
    """serializer for movies ratings."""
    Source = serializers.CharField(source='source')
    Value = serializers.CharField(source='value')

    class Meta:
        model = Rating
        fields = ('Source', 'Value')


class MoviesSerializer(serializers.ModelSerializer):
    """ serializes data from omdbapi. All fields are included also relational field ratings."""

    ratings = RatingSerializer(many=True)

    def create(self, validated_data):
        ratings_data = validated_data.pop('ratings')
        movie = Movie.objects.create(**validated_data)
        for rating in ratings_data:
            Rating.objects.create(movie=movie, **rating)
        return movie

    class Meta:
        model = Movie
        exclude = ('id',)


class CommentSerializer(serializers.ModelSerializer):
    """Serializes users comments."""

    class Meta:
        model = Comment
        fields = '__all__'
