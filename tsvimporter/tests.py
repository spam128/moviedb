from django.test import TestCase
from tsvimporter.reader import tsv_reader

class TestTsvImporter(TestCase):
    def test_read_title_tsv(self):
        # with TsvReader('/home/corpuscallosum/workspace/moviedb/title.basics.tsv') as tsv:
        #     print('hello')
        # tsv_reader('')
        # for row in tsv_reader('/home/corpuscallosum/workspace/moviedb/title.basics.tsv'):
        #     print(row)
        i=0
        with tsv_reader('/home/corpuscallosum/workspace/moviedb/title.basics.tsv.gz') as tsv:
            #columns = next(tsv)
            print(tsv['columns'])
            for row in tsv['reader']:
                print(row)
                i+=1
                if i==10:
                    break
        self.assertFalse()

    def test_read_name_tsv(self):
        # with TsvReader('/home/corpuscallosum/workspace/moviedb/title.basics.tsv') as tsv:
        #     print('hello')
        # tsv_reader('')
        # for row in tsv_reader('/home/corpuscallosum/workspace/moviedb/title.basics.tsv'):
        #     print(row)
        i=0
        with tsv_reader('/home/corpuscallosum/workspace/moviedb/name.basics.tsv.gz') as tsv:
            print(tsv['columns'])
            for row in tsv['reader']:
                print(row)
                i+=1
                if i==10:
                    break
        self.assertFalse()

    def test_opening_non_existing_file_rise_error(self):
        with self.assertRaises(FileNotFoundError):
            with tsv_reader('non-existing-file') as tsv:
                print(tsv)
