from django.db import models


class Titles(models.Model):
    """
    title.basics.tsv.gz - Contains the following information for titles:
        tconst (string) - alphanumeric unique identifier of the title
        titleType (string) – the type/format of the title (e.g. movie, short, tvseries, tvepisode, video, etc)
        primaryTitle (string) – the more popular title / the title used by the filmmakers on promotional materials at the point of release
        originalTitle (string) - original title, in the original language
        isAdult (boolean) - 0: non-adult title; 1: adult title
        startYear (YYYY) – represents the release year of a title. In the case of TV Series, it is the series start year
        endYear (YYYY) – TV Series end year.'\\N' for all other title types
        runtimeMinutes – primary runtime of the title, in minutes
        genres (string array) – includes up to three genres associated with the title
    """
    IS_ADULT_CHOICES = (('0', False), ('1', True))

    tconst = models.CharField(max_length=10, unique=True, help_text='Alphanumeric unique identifier of the title')
    titleType = models.CharField(
        max_length=15,
        default='',
        help_text='The type/format of the title (e.g. movie, short, tvseries, tvepisode, video, etc)')
    primaryTitle = models.CharField(
        max_length=1000,
        default='',
        help_text='The more popular title / the title used by the filmmakers on promotional materials at the point of release')
    originalTitle = models.CharField(
        max_length=1000,
        default='',
        help_text='Original title, in the original language')
    isAdult = models.BooleanField(
        choices=IS_ADULT_CHOICES,
        default=False,
        help_text='False: non-adult title; True: adult title')
    startYear = models.CharField(
        max_length=5,
        default='',
        help_text='Represents the release year of a title. In the case of TV Series, it is the series start year')
    endYear = models.CharField(
        max_length=5,
        default='\\N',
        help_text='TV Series end year. \\N for all other title types')
    runtimeMinutes = models.CharField(
        max_length=5,
        default='\\N',
        help_text='Primary runtime of the title, in minutes')
    genres = models.CharField(
        max_length=500,
        default='',
        help_text='Includes up to three genres associated with the title')

    def __str__(self):
        if self.originalTitle:
            return self.originalTitle
        else:
            return self.tconst

    class Meta:
        ordering = ('primaryTitle',)


class Names(models.Model):
    """
    name.basics.tsv.gz – Contains the following information for names:
        nconst (string) - alphanumeric unique identifier of the name/person
        primaryName (string)– name by which the person is most often credited
        birthYear – in YYYY format
        deathYear – in YYYY format if applicable, else '\\N'
        primaryProfession (array of strings)– the top-3 professions of the person
        knownForTitles (array of tconsts) – titles the person is known for
    """
    nconst = models.CharField(max_length=10, unique=True, help_text='Alphanumeric unique identifier of the name/person')
    primaryName = models.CharField(
        max_length=300,
        default='',
        help_text='Name by which the person is most often credited')
    birthYear = models.CharField(
        max_length=5,
        default='',
        help_text='In YYYY format')
    deathYear = models.CharField(
        max_length=5,
        default='',
        help_text='In YYYY format if applicable, else \\N')
    primaryProfession = models.CharField(
        max_length=500,
        default='',
        help_text='the top-3 professions of the person')
    knownForTitles = models.ManyToManyField(
        Titles,
        related_name='names',
        blank=True,
        default=None,
        help_text='titles the person is known for')

    def __str__(self):
        if self.primaryName:
            return self.primaryName
        else:
            return self.nconst

    class Meta:
        ordering = ('nconst',)
