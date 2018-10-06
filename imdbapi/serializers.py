from rest_framework import serializers
from imdbapi.models import Titles, Names


class TitlesSerializer(serializers.ModelSerializer):
    """Serializes movie Titles from imdb."""

    class Meta:
        model = Titles
        fields = '__all__'


class NamesSerializer(serializers.ModelSerializer):
    """Serializes names from imdb."""

    def to_internal_value(self, data):
        """
        Attribute with many to many relation have list films as an string but needed as list.
        Conversion is needed before data is validated.
        """
        if isinstance(data['knownForTitles'], str):
            data['knownForTitles'] = data['knownForTitles'].split(',')
        return data

    def create(self, validated_data):
        """
        Create Name instance, if related model Title is not present, creates empty one with given unique number.
        """
        known_for_titles = validated_data.pop('knownForTitles', [])
        titles = [Titles.objects.get_or_create(tconst=tconst)[0] for tconst in known_for_titles]
        model = Names.objects.create(**validated_data)
        model.knownForTitles.set(titles)
        return model

    class Meta:
        model = Names
        fields = '__all__'
