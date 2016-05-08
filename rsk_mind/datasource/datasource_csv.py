import csv
from datasource import Datasource
from ..dataset import Dataset

class CSVDatasource(Datasource):

    def __init__(self, path, target=None):
        super(CSVDatasource, self).__init__(path)
        self.target = target

    def read(self):
        with open(self.path, 'rb') as infile:
            reader = csv.reader(infile)

            header = reader.next()

            rows = []
            for row in reader:
                if self.target is not None:
                    index = header.index(self.target)
                    target = row[index]
                    del row[index]
                    row += [target]
                rows.append(row)

        return Dataset(header, rows)


    def write(self, dataset):
        with open(self.path, 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(dataset.transformed_header)

            for row in dataset.transformed_rows:
                writer.writerow(row)
