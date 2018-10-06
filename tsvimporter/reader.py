import csv
import contextlib
import gzip


@contextlib.contextmanager
def tsv_reader(path):
    """
    Context manager which reads data from TSV files (also from packed with gzip ones.
    Returns dict keys[columns, reader] with columns and iterator, next ones are lists of values

    Keyword parameters:
        path -- path of file which is going to be read
    """
    if path[-3:] == '.gz':
        with gzip.open(path, 'rt') as tsv_file:
            data = csv.reader(tsv_file, delimiter='\t')
            columns = next(data)
            yield {'columns': columns, 'reader': data}
    else:
        with open(path) as tsv_file:
            data = csv.reader(tsv_file, delimiter='\t')
            columns = next(data)
            yield {'columns': columns, 'reader': data}



