from rest_framework import viewsets
from imdbapi.models import Titles, Names
from imdbapi.serializers import TitlesSerializer, NamesSerializer
from rest_framework.filters import OrderingFilter, SearchFilter


class TitlesViewSet(viewsets.ModelViewSet):
    """Viewset for retrieving movies titles"""
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    filter_backends = (SearchFilter,)  # OrderingFilter
    search_fields = ('genres', 'startYear', 'names__primaryName')
    ordering = ('primaryTitle',)


class NamesViewSet(viewsets.ModelViewSet):
    """Viewset for retrieving movies titles"""
    queryset = Names.objects.all()
    serializer_class = NamesSerializer
    filter_backends = (SearchFilter,)  # OrderingFilter
    search_fields = ('genres', 'startYear')
    ordering = ('primaryTitle',)

# Pobrać listę - wg kolejności alfabetycznej - wszystkich tytułów filmów o wskazanej wartości startYear, wraz z powiązanymi z nimi osobami (mechanizm z paginacją wyników).

# Jak wyżej, ale z możliwością wylistowania filmów z wskazanym genre.

# Zwrócić filmy, z którymi związane są osoby pasujące do wyników wyszukiwania(czyli jako parametr przekazujemy frazę - np. z nazwiskiem, na podstawie której szukamy ludzi i dla każdego z nich zwracamy listę tytułów filmów).
