from django.test import TestCase
from tsvimporter.reader import TsvReader


class TestTsvImporter(TestCase):
    def test_read_title_tsv_in_gzip(self):
        expedted_columns = ['tconst', 'titleType', 'primaryTitle', 'originalTitle', 'isAdult', 'startYear', 'endYear',
                            'runtimeMinutes', 'genres']
        expected_rows = [
            ['tt0000001', 'short', 'Carmencita', 'Carmencita', '0', '1894', '\\N', '1', 'Documentary,Short'],
            ['tt0000002', 'short', 'Le clown et ses chiens', 'Le clown et ses chiens', '0', '1892', '\\N', '5',
             'Animation,Short'],
            ['tt0000003', 'short', 'Pauvre Pierrot', 'Pauvre Pierrot', '0', '1892', '\\N', '4',
             'Animation,Comedy,Romance']
        ]
        i = 0
        with TsvReader('title.basics.tsv.gz') as tsv:
            self.assertEqual(tsv.columns, expedted_columns)
            for row in tsv.readline():
                self.assertEqual(row, expected_rows[i])
                i += 1
                if i == 2:
                    break

    def test_read_name_tsv_in_gzip(self):
        expedted_columns = ['nconst', 'primaryName', 'birthYear', 'deathYear', 'primaryProfession', 'knownForTitles']

        expected_rows = [
            ['nm0000001', 'Fred Astaire', '1899', '1987', 'soundtrack,actor,miscellaneous',
             'tt0120689,tt0028333,tt0050419,tt0027125'],
            ['nm0000002', 'Lauren Bacall', '1924', '2014', 'actress,soundtrack',
             'tt0037382,tt0038355,tt0040506,tt0055688'],
            ['nm0000003', 'Brigitte Bardot', '1934', '\\N', 'actress,soundtrack,producer',
             'tt0063715,tt0049189,tt0057345,tt0059956']
        ]
        i = 0
        with TsvReader('name.basics.tsv.gz') as tsv:
            self.assertEqual(tsv.columns, expedted_columns)
            for row in tsv.readline():
                self.assertEqual(row, expected_rows[i])
                i += 1
                if i == 2:
                    break

    def test_opening_non_existing_file_rises_error(self):
        with self.assertRaises(FileNotFoundError):
            with TsvReader('non-existing-file.tsv') as tsv:
                print(tsv)

    def test_opening_non_existing_file_rises_error(self):
        with self.assertRaises(FileNotFoundError):
            with TsvReader('non-existing-file.tsv.gz') as tsv:
                print(tsv)

    def test_open_wrong_extension(self):
        with self.assertRaises(ValueError):
            with TsvReader('s') as tsv:
                print(tsv)
