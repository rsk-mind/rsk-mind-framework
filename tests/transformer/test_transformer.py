import os

from nose.tools import assert_equals, assert_items_equal
from rsk_mind.dataset import Dataset
from rsk_mind.transformer import *


class CustomTransformer(Transformer):

    class Feats:
        a1 = Feat()
        a2 = Feat()
        f1 = CompositeFeat(['a1', 'a2'])

    def get_a1(self, feat):
        return [-float(feat)]

    def get_a2(self, feat):
        return [-float(feat)]

    def get_f1(self, a1, a2):
        return [float(a1) + float(a2)]


class TestDataset:

    def setUp(self):
        self.header = ['a1', 'a2', 'y']
        self.rows = [['0', '0', '0'], ['0', '2', '0'], ['1', '0.5', '1'], ['0.9', '2', '1']]
        self.transformer = CustomTransformer()

    def tearDown(self):
        # delete variables to release memory
        del self.header
        del self.rows
        del self.transformer

    def test_get_feats(self):
        _expected_feats = ['a1', 'a2', 'f1']
        _actual_feats = self.transformer.get_feats()
        assert_items_equal(_expected_feats, _actual_feats)

    def test_get_transformer_func(self):
        _expected_value = [-2]
        _actual_value = self.transformer.get_transformer_func('a1')(2)

        assert_items_equal(_expected_value, _actual_value)
