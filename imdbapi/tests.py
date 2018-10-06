from django.test import TestCase
from django.core.management import call_command
from imdbapi.models import Titles, Names


class TestIMDBRestApi(TestCase):
    def test_(self):
        self.assertFalse('')


class TestCommands(TestCase):
    def test_loadimdbtsv(self):
        call_command('loadimdbtsv', 'title.basics.tsv.gz', 'name.basics.tsv.gz')
        self.assertEqual(Titles.objects.count(), 15)
        self.assertFalse()

    def test_loadimdbtsv_with_existing_unique_number(self):
        pass
