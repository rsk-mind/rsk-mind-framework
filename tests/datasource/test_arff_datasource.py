from nose.tools import assert_equals
from rsk_mind.datasource import ArffDatasource
from rsk_mind.dataset import Dataset
import os


class TestArffDatasource:

    def setUp(self):
        self.in_path = os.path.join(os.getcwd(), 'tests/files/in.arff')
        self.out_path = os.path.join(os.getcwd(), 'tests/files/out.arff')

    def tearDown(self):
        # delete the out file if it exists
        if os.path.exists(self.out_path):
            os.remove(self.out_path)
        # delete variables to release memory
        del self.in_path
        del self.out_path

    def test_read(self):
        arff_dsrc = ArffDatasource(self.in_path)
        arff_dataset = arff_dsrc.read()

        _header = arff_dataset.header
        _rows = arff_dataset.rows

        # check header length
        assert_equals(len(_header), 5)

        # check number of rows
        assert_equals(len(_rows), 3)

    def test_write(self):
        # create a dataset
        _header = ['feat0', 'feat1', 'feat2', 'target']
        _rows = [[0, 1, 0, 0], [1, 1, 0, 1]]
        arff_dataset = Dataset(_header, _rows)
        arff_dataset.transformed_header = _header
        arff_dataset.transformed_rows = _rows

        arff_dsrc = ArffDatasource(self.out_path)

        # write dataset to file
        arff_dsrc.write(arff_dataset)

        # check if file is created
        response = os.path.exists(self.out_path) and os.path.isfile(self.out_path)

        assert_equals(response, True)
