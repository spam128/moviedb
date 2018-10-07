from rest_framework import serializers
from imdbapi.models import Titles, Names


class NamesSerializer(serializers.ModelSerializer):
    """Serializes names from imdb."""
    knownForTitles = serializers.StringRelatedField(many=True)

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
        If the process is interrupted, calling it again bypass existing instances.
        """
        known_for_titles = validated_data.pop('knownForTitles', [])
        titles = [Titles.objects.get_or_create(tconst=tconst)[0] for tconst in known_for_titles]
        model, created = Names.objects.get_or_create(**validated_data)
        if created:
            model.knownForTitles.set(titles)
        return model

    class Meta:
        model = Names
        fields = '__all__'


class TitlesSerializer(serializers.ModelSerializer):
    """
    Serializes movie Titles from imdb.
    If instance is created because NameSerializer had a person connected with that movie, instance is updated
    """
    names = NamesSerializer(many=True, required=False)

    def create(self, validated_data):
        """create or update instance"""
        instance, _ = Titles.objects.update_or_create(**validated_data)
        return instance

    class Meta:
        model = Titles
        fields = '__all__'
