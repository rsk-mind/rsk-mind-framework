import csv

import pandas as pd

from datasource import DataSource
from ..dataset import PandasDataset


class CSVStreamDataSource(DataSource):
    """Parse and read a data source on CSV Format as a stream.
    """

    def __init__(self, path, chunk=10, target=None):
        """Create a new CSV Stream DataSource with target class name.

        :param path: a path to CSV file.
        :param target: target class name is optional.
        """
        super(CSVStreamDataSource, self).__init__(path)
        self.target = target
        self.chunk = chunk

    def read(self):
        """Read a data source on CSV format as a stream.

        Always place target class on last column.

        :return: a dataset.
        """
        reader = pd.read_table(self.path, sep=',', chunksize=self.chunk)
        return PandasDataset(reader)

    def write(self, dataset, write_transformed=True):
        """Write data on file with csv format as a stream.

        If transformation had applied on dataset write transformed data
        otherwise the same dataset.

        :param dataset:
        :param write_transformed:
        """
        if write_transformed:
            print write_transformed
            header = dataset.transformed_header
            rows = dataset.transformed_rows

            with open(self.path, 'w') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(header)

                for row in rows:
                    writer.writerow(row)
        else:
            raise Exception('')
