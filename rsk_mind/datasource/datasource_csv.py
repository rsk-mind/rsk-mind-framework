import csv
from datasource import Datasource
from ..dataset import Dataset

class CSVDatasource(Datasource):

    def read(self):
        with open(self.path, 'rb') as infile:
            reader = csv.reader(infile)

            header = reader.next()

            rows = []
            for row in reader:
                rows.append(row)

        return Dataset(header, rows)


    def write(self, dataset):
        with open(self.path, 'w') as outfile:

            print >> outfile, ",".join(dataset.header)

            for row in dataset.rows:
                print >> outfile, ",".join(row)
