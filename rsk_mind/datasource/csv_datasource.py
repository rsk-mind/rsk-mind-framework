from . import Datasource

import csv

class CSVDatasource(Datasource):

    def __init__(self, path, has_header=True):
        self.path = path


    def read(self):
        """ """
        with open(self.path, 'rb') as csvfile:
            rows_reader = csv.reader(csvfile)

            if self.has_header:
                self.header = rows_reader.next()

            for row in rows_reader:
                self.rows.append(row)

    def write(self, dataset):
        pass
