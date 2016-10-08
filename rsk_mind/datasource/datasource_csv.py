import csv

from datasource import DataSource
from ..dataset import Dataset


class CSVDataSource(DataSource):
    """Handle CSV formatted datasource.

    All the methods to handle a CSV formatted datasource.
    """

    def __init__(self, path, target=None):
        """Create a new CSV Datasource with target class name.

        :param path: a path to CSV file.
        :param target: target class name is optional.
        """
        super(CSVDataSource, self).__init__(path)
        self.target = target

    def read(self):
        """Read a data source on CSV format.

        Always place target class on last column.

        :return: a dataset.
        """
        with open(self.path, 'rb') as infile:
            reader = csv.reader(infile)

            header = reader.next()

            rows = []
            for row in reader:
                if self.target is not None:
                    try:
                        index = header.index(self.target)
                    except:
                        raise Exception('Target class not found')
                    target = row[index]
                    del row[index]
                    row += [target]

                rows.append(row)

            if self.target is not None:
                index = header.index(self.target)
                tmp = header[index]
                del header[index]
                header += [tmp]

        return Dataset(header, rows)

    def write(self, dataset, write_transformed=True):
        """Write data on file with csv format.

        If transformation had applied on dataset write transformed data
        otherwise the same dataset.

        :param dataset:
        :param write_transformed:
        """
        if dataset.transformed_header is None or not write_transformed:
            header = dataset.header
            rows = dataset.rows
        else:
            header = dataset.transformed_header
            rows = dataset.transformed_rows

        with open(self.path, 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)

            for row in rows:
                writer.writerow(row)
