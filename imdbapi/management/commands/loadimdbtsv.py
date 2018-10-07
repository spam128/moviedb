from django.core.management.base import BaseCommand
import logging

from tsvimporter.reader import TsvReader
from imdbapi.serializers import TitlesSerializer, NamesSerializer

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Loads given tsv from imdb with titles and names into database

    usage:
        python manage.py loadimdbtsv file_path file_path
    """
    help = 'Load tsv files data with titles/names to database. ' \
           'Any string after commad should be a path to tsv file or tsv file compresed by gzip'
    max_bulk = 10

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **options):
        for path in options['path']:
            with TsvReader(path) as tsv:
                if 'primaryTitle' in tsv.columns:
                    serializer = TitlesSerializer
                if 'primaryName' in tsv.columns:
                    serializer = NamesSerializer
                self.save_to_db(tsv, serializer)

    def save_to_db(self, tsv, serializer):
        """save data to database in parts, max size is taken from self.max_bulk
        Keyword arguments:
            tsv -- tsv file opened in tsvimporter
            serializer -- serializer which is going to be used to validate data
        """
        bulk_models = []
        counter = 0

        for row in tsv.readline():
            bulk_models.append({k: v for k, v in zip(tsv.columns, row)})
            counter += 1
            if not counter % self.max_bulk:
                self.bulk_save(serializer, bulk_models, counter)
                bulk_models = []

        if not counter % self.max_bulk:
            return
        self.bulk_save(serializer, bulk_models, counter)

    @staticmethod
    def bulk_save(serializer, bulk_models, counter):
        """
        Save part of processed models

        Keyword params:
            serializer - serializer used to validate and save data
            bulk_models - list of models to be saved
            counter - how many models were processed
        """
        serialized_data = serializer(data=bulk_models, many=True)
        serialized_data.is_valid()
        serialized_data.save()
        logger.info('Saved {} rows'.format(counter))
        print('Saved {} rows'.format(counter))
