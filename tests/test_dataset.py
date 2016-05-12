import os

from nose.tools import assert_equals
from rsk_mind.datasource import CSVDatasource
from rsk_mind.dataset import Dataset

class TestDataset:

    def setUp(self):
        self.header = ['a1', 'a2', 'y']
        self.rows = [['0', '0', '1'], ['0', '2', '1'], ['1', '0.5', '1'] ,['0.9', '2', '1']]

    def tearDown(self):
        # delete variables to release memory
        del self.header
        del self.rows
