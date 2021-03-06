# Generated by Django 2.1.1 on 2018-10-06 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nconst', models.CharField(help_text='Alphanumeric unique identifier of the name/person', max_length=10, unique=True)),
                ('primaryName', models.CharField(default='', help_text='Name by which the person is most often credited', max_length=300)),
                ('birthYear', models.CharField(default='', help_text='In YYYY format', max_length=5)),
                ('deathYear', models.CharField(default='', help_text='In YYYY format if applicable, else \\N', max_length=5)),
                ('primaryProfession', models.CharField(default='', help_text='the top-3 professions of the person', max_length=100)),
            ],
            options={
                'ordering': ('nconst',),
            },
        ),
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tconst', models.CharField(help_text='Alphanumeric unique identifier of the title', max_length=10, unique=True)),
                ('titleType', models.CharField(default='', help_text='The type/format of the title (e.g. movie, short, tvseries, tvepisode, video, etc)', max_length=15)),
                ('primaryTitle', models.CharField(default='', help_text='The more popular title / the title used by the filmmakers on promotional materials at the point of release', max_length=150)),
                ('originalTitle', models.CharField(default='', help_text='Original title, in the original language', max_length=150)),
                ('isAdult', models.BooleanField(default=False, help_text='False: non-adult title; True: adult title')),
                ('startYear', models.CharField(default='', help_text='Represents the release year of a title. In the case of TV Series, it is the series start year', max_length=5)),
                ('endYear', models.CharField(default='\\N', help_text='TV Series end year. \\N for all other title types', max_length=5)),
                ('runtimeMinutes', models.CharField(default='\\N', help_text='Primary runtime of the title, in minutes', max_length=5)),
                ('genres', models.CharField(default='', help_text='Includes up to three genres associated with the title', max_length=100)),
            ],
            options={
                'ordering': ('tconst',),
            },
        ),
        migrations.AddField(
            model_name='names',
            name='knownForTitles',
            field=models.ManyToManyField(blank=True, default=None, help_text='titles the person is known for', to='imdbapi.Titles'),
        ),
    ]
