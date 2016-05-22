from nose.tools import assert_equals, assert_items_equal, assert_raises
from rsk_mind.datasource import CSVDataSource
from rsk_mind.dataset import Dataset
import os


class TestCsvDatasource:
    def __init__(self):
        self.out_path = os.path.join(os.getcwd(), 'tests/files/out.csv')
        self.in_path = os.path.join(os.getcwd(), 'tests/files/in.csv')

    def setUp(self):
        # delete the out file if it exists
        if os.path.exists(self.out_path):
            os.remove(self.out_path)

    def tearDown(self):
        # delete variables to release memory
        del self.in_path
        del self.out_path

    def test_read_target(self):
        csv_datasource = CSVDataSource(self.in_path, target='a1')
        csv_dataset = csv_datasource.read()

        _expected_header = ['a2', 'a3', 'a4', 'target', 'a1']
        _expected_rows = [['0', '0', '0', '1', '0'], ['1', '0', '1', '0', '1'], ['0', '0', '1', '0',
                                                                                 '1']]

        _header = csv_dataset.header
        _rows = csv_dataset.rows

        # check _header array
        assert_items_equal(_header, _expected_header)

        # check _row matrices
        assert_items_equal(_rows, _expected_rows)

        csv_datasource = CSVDataSource(self.in_path, target='a5')

        assert_raises(Exception, csv_datasource.read)

    def test_read(self):
        csv_datasource = CSVDataSource(self.in_path)
        csv_dataset = csv_datasource.read()

        _expected_header = ['a1', 'a2', 'a3', 'a4', 'target']
        _expected_rows = [['0', '0', '0', '0', '1'], ['1', '1', '0', '1', '0'], ['1', '0', '0', '1', '0']]

        _header = csv_dataset.header
        _rows = csv_dataset.rows

        # check _header array
        assert_items_equal(_header, _expected_header)

        # check _row matrices
        assert_items_equal(_rows, _expected_rows)

    def test_write(self):
        # create a dataset
        _header = ['feat0', 'feat1', 'feat2', 'target']
        _rows = [['0', '1', '0', '0'], ['1', '1', '0', '1']]
        csv_dataset = Dataset(_header, _rows)

        csv_datasource = CSVDataSource(self.out_path)

        # write dataset to file
        csv_datasource.write(csv_dataset)

        # check if file is created
        response = os.path.exists(self.out_path) and os.path.isfile(self.out_path)

        assert_equals(response, True)

    def test_write_transformed(self):
        # create a dataset
        _header = ['feat0', 'feat1', 'feat2', 'target']
        _rows = [['0', '1', '0', '0'], ['1', '1', '0', '1']]
        csv_dataset = Dataset(None, None)

        csv_dataset.transformed_header = _header
        csv_dataset.transformed_rows = _rows

        csv_datasource = CSVDataSource(self.out_path)

        # write dataset to file
        csv_datasource.write(csv_dataset)

        # check if file is created
        response = os.path.exists(self.out_path) and os.path.isfile(self.out_path)

        assert_equals(response, True)