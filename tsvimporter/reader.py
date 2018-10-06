import csv
import gzip


class TsvReader:
    """
    Context manager which reads data from TSV files (also from packed with gzip ones.
    Returns dict keys[columns, reader] with columns and iterator, next ones are lists of values

    Keyword parameters for initialization:
        path -- path of file which is going to be read

    example use, print all data rows:
    with TsvReader('tsv-file.tsv') as tsv:
        for row in tsv.readline():
            print(row)
    """

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.file = self.open(self.path)
        self.data = csv.reader(self.file, delimiter='\t')
        self.columns = next(self.data)
        return self

    def __exit__(self, *args):
        self.file.__exit__(*args)

    @staticmethod
    def open(path):
        """open given file, can be compresed by gzip"""
        if path.endswith('.gz'):
            return gzip.open(path, 'rt')
        elif path.endswith('.tsv'):
            return open(path)
        else:
            raise ValueError('Wrong file extension')

    def readline(self):
        """returns tsv data iterator"""
        return self.data
