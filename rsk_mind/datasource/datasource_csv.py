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
            writer = csv.writer(outfile)
            writer.writerow(dataset.transformed_header)
            
            for row in dataset.transformed_rows:
                writer.writerow(row)
