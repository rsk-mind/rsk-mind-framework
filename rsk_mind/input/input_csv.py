from .input import Input

import csv


class CSVInput(Input):

    def __init__(self, path, has_header=True):
        self.path = path
        self.has_header = has_header
        self.rows = []


    def read(self):
        """ """
        with open(self.path, 'rb') as csvfile:
            rows_reader = csv.reader(csvfile)

            if self.has_header:
                self.header = rows_reader.next()

            for row in rows_reader:
                self.rows.append(row)
