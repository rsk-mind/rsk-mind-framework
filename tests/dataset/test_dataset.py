from nose.tools import assert_equals, assert_items_equal

from rsk_mind.dataset import Dataset
from rsk_mind.transformer import *


class CustomTransformer(Transformer):
    class Feats():
        a1 = Feat()
        a2 = Feat()

        f1 = CompositeFeat(['a1', 'a2'])

    def get_a1(self, feat):
        return [-float(feat), 'a1']

    def get_a2(self, feat):
        return [-float(feat)]

    def get_f1(self, a1, a2):
        return [float(a1) + float(a2)]


class TestDataset:

    def setUp(self):
        self.header = ['a1', 'a2', 'y']
        self.rows = [['0', '0', '0'], ['0', '2', '0'], ['1', '0.5', '1'] ,['0.9', '2', '1']]

    def tearDown(self):
        # delete variables to release memory
        del self.header
        del self.rows

    def test_init(self):
        _dataset = Dataset(self.header, self.rows)

        assert_items_equal(_dataset.header, self.header)
        assert_items_equal(_dataset.rows, self.rows)
        assert_items_equal(_dataset.transformed_rows, [])
        assert_equals(_dataset.transformer, None)
        assert_equals(_dataset.transformed_header, None)

    def test_setTransformer(self):
        _dataset = Dataset(self.header, self.rows)
        _transformer = CustomTransformer()
        _dataset.setTransformer(_transformer)

        assert_equals(_dataset.transformer, _transformer)

    def test_applyTransformations(self):
        _dataset = Dataset(self.header, self.rows)
        _transformer = CustomTransformer()
        _dataset.setTransformer(_transformer)

        _header = ['a1_0', 'a1_1', 'a2', 'f1', 'y']
        _rows = [[0, 'a1', 0, 0, '0'], [0, 'a1', -2, 2, '0'], [-1, 'a1', -0.5, 1.5, '1'],[-0.9, 'a1', -2, 2.9, '1']]

        _dataset.applyTransformations()

        assert_items_equal(_dataset.header, self.header)
        assert_items_equal(_dataset.rows, self.rows)
        assert_equals(_dataset.transformed_header, _header)
        assert_items_equal(_dataset.transformed_rows, _rows)
        assert_equals(_dataset.transformer, _transformer)

    def test_applyTransformations_Without_Transformer(self):
        _dataset = Dataset(self.header, self.rows)

        _header = ['a1', 'a2', 'y']
        _rows = [['0', '0', '0'], ['0', '2', '0'], ['1', '0.5', '1'], ['0.9', '2', '1']]

        _dataset.applyTransformations()

        assert_items_equal(_dataset.header, self.header)
        assert_items_equal(_dataset.rows, self.rows)
        assert_equals(_dataset.transformed_header, _header)
        assert_items_equal(_dataset.transformed_rows, _rows)
        assert_equals(_dataset.transformer, None)