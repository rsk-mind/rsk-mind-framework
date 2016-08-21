import json

from datasource import DataSource
from ..dataset import Dataset


class JSONDataSource(DataSource):
    """Parse and read a data source on JSON Format.
    """

    def __init__(self, path, target=None):
        """Create a new JSON Datasource with targe class name.

        Target class name is optional.

        :param path: a path to CSV file.
        :param target: target class name is optional.
        """
        super(JSONDataSource, self).__init__(path)
        self.target = target

    def read(self):
        """Read a data source on JSON format.

        Always place target class on last column.

        :return: a dataset.
        """
        with open(self.path, 'rb') as infile:
            reader = json.load(infile)

            header = None
            rows = []
            for row in reader:
                if not header:
                    header = row.keys()

                _row = row.values()
                try:
                    index = header.index(self.target)
                    _target = _row[index]
                    del _row[index]
                    _row += [_target]
                    rows.append(_row)
                except:
                    raise Exception('Target class not found')

            try:
                index = header.index(self.target)

                _tmp = header[index]
                del header[index]
                header += [_tmp]
            except:
                raise Exception('Target class not found')
        return Dataset(header, rows)

    def write(self, dataset, write_transformed=True):
        """Write data on file with JSON format.

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
            _rows = []

            for row in rows:
                tmp = {}
                for i, attr in enumerate(header):
                    tmp[attr] = row[i]

                _rows.append(tmp)

            json.dump(_rows, outfile)
