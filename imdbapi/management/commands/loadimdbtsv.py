from django.core.management.base import BaseCommand, CommandError
from tsvimporter.reader import tsv_reader

class Command(BaseCommand):
    help = 'Load csv file data to database'

    def add_arguments(self, parser):
        parser.add_argument()

    def handle(self, *args, **options):
        pass