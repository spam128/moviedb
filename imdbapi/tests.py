from django.test import TestCase
from django.core.management import call_command
from imdbapi.models import Titles, Names
from tsvimporter.tests.tests import NAME_DATA


class TestIMDBRestApi(TestCase):
    def test_(self):
        self.assertFalse('')


class TestCommands(TestCase):
    test_data_path = 'tsvimporter/tests/data'

    def test_loadimdbtsv(self):
        call_command('loadimdbtsv',
                     '{path}/test.title.basics.tsv.gz'.format(path=self.test_data_path),
                     '{path}/test.name.basics.tsv.gz'.format(path=self.test_data_path))
        self.assertEqual(Titles.objects.count(), 15)
        self.assertEqual(Names.objects.count(), 3)
        instance = Names.objects.filter(primaryName='Fred Astaire')[0]
        self.assertEqual(NAME_DATA['rows'][0][0], instance.nconst)
        self.assertEqual(NAME_DATA['rows'][0][1], instance.primaryName)
        self.assertEqual(NAME_DATA['rows'][0][2], instance.birthYear)
        self.assertEqual(NAME_DATA['rows'][0][3], instance.deathYear)
        self.assertEqual(NAME_DATA['rows'][0][4], instance.primaryProfession)
