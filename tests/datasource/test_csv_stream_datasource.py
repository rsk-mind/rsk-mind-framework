from nose.tools import assert_equals, assert_items_equal, assert_raises
from rsk_mind.datasource import CSVStreamDataSource
from rsk_mind.dataset import Dataset, PandasDataset
import os


class TestCSVStreamDataSource:
    def __init__(self):
        self.in_path = os.path.join(os.getcwd(), 'tests/files/in.csv')
        self.out_path = os.path.join(os.getcwd(), 'tests/files/out.stream.csv')

    def setUp(self):
        # delete the out file if it exists
        if os.path.exists(self.out_path):
            os.remove(self.out_path)

    def tearDown(self):
        # delete variables to release memory
        del self.in_path
        del self.out_path

    def test_read(self):
        _expected_chunk = 10000
        _expected_target = None

        csv_datasource = CSVStreamDataSource(self.in_path, _expected_chunk)
        csv_dataset = csv_datasource.read()

        _expected_header = ['a1', 'a2', 'a3', 'a4', 'target']
        _expected_rows = [[0, 0, 0, 0, 1], [1, 1, 0, 1, 0], [1, 0, 0, 1, 0]]

        _pandas_reader = csv_dataset.reader

        _pandas_df = _pandas_reader.next()

        _header = list(_pandas_df.columns)

        _rows = []
        for index, row in _pandas_df.iterrows():
            _rows.append(list(row))

        assert_equals(csv_datasource.chunk, _expected_chunk)
        assert_equals(csv_datasource.target, _expected_target)

        assert_items_equal(_header, _expected_header)
        assert_items_equal(_rows, _expected_rows)

    def test_write_original_dataset(self):
        csv_datasource = CSVStreamDataSource(None)
        csv_dataset = Dataset(None, None)

        assert_raises(Exception, csv_datasource.write, csv_dataset, False)

    def test_write(self):
        csv_dataset = PandasDataset(None)

        _expected_header = ['a1', 'a2', 'a3', 'a4', 'target']
        _expected_rows = [[0, 0, 0, 0, 1], [1, 1, 0, 1, 0], [1, 0, 0, 1, 0]]

        csv_dataset.transformed_header = _expected_header
        csv_dataset.transformed_rows = _expected_rows

        csv_datasource = CSVStreamDataSource(self.out_path)

        # write dataset to file
        csv_datasource.write(csv_dataset)

        # check if file is created
        response = os.path.exists(self.out_path) and os.path.isfile(self.out_path)
        assert_equals(response, True)

        _expected_chunk = 10000
        _expected_target = None

        csv_datasource = CSVStreamDataSource(self.out_path, _expected_chunk)
        csv_dataset = csv_datasource.read()

        _pandas_reader = csv_dataset.reader

        _pandas_df = _pandas_reader.next()

        _header = list(_pandas_df.columns)

        _rows = []
        for index, row in _pandas_df.iterrows():
            _rows.append(list(row))

        assert_equals(csv_datasource.chunk, _expected_chunk)
        assert_equals(csv_datasource.target, _expected_target)

        assert_items_equal(_header, _expected_header)
        assert_items_equal(_rows, _expected_rows)
