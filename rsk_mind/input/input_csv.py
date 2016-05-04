from .input import Input


class CSVInput(Input):

    def __init__(self, path, has_header=True):
        self.path = path
        self.has_header = has_header
        self.rows = []


    def read(self):
        """ """
        with open(self.path, 'rb') as csvfile:
            import csv
            print csv
            rows_reader = csv.reader(csvfile)

            if self.has_header:
                self.header = rows_reader.next()

            for row in rows_reader:
                self.rows.append(row)


    def transform(self, transformer, output=None):
        """ """
        raise NotImplementedError("")


    def classify(self, classifier, output=None):
        """ """
        raise NotImplementedError("")
