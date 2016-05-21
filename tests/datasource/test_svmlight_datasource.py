from nose.tools import assert_equals
from rsk_mind.datasource import SVMLightDataSource
from rsk_mind.dataset import Dataset
import os

class TestSVMLightDatasource:

    def setUp(self):
        self.in_path = os.path.join(os.getcwd(),'tests/files/in.dat')
        self.out_path = os.path.join(os.getcwd(),'tests/files/out.dat')

    def tearDown(self):
        # delete the out file if it exists
        if os.path.exists(self.out_path):
            os.remove(self.out_path)
        # delete variables to release memory
        del self.in_path
        del self.out_path

    def test_read(self):
        svm_dsrc = SVMLightDataSource(self.in_path)
        svm_dataset = svm_dsrc.read()

        _header = svm_dataset.header
        _rows = svm_dataset.rows

        # check header length
        assert_equals(len(_header), 5)

        # check number of rows
        assert_equals(len(_rows), 3)

    def test_write(self):
        # create a dataset
        _header = ['feat0', 'feat1', 'feat2', 'target']
        _rows = [[0, 1, 0, 0], [1, 1, 0, 1]]
        svm_dataset = Dataset(_header, _rows)
        svm_dataset.transformed_header = _header
        svm_dataset.transformed_rows = _rows

        svm_dsrc = SVMLightDataSource(self.out_path)

        # write dataset to file
        svm_dsrc.write(svm_dataset)

        # check if file is created
        response = os.path.exists(self.out_path) and os.path.isfile(self.out_path)

        assert_equals(response, True)
