from nose.tools import assert_raises

from rsk_mind.datasource import DataSource


class TestDatasource:
    def __init__(self):
        self.datasource = DataSource("dummy path")

    def test_read(self):
        assert_raises(NotImplementedError, self.datasource.read)

    def test_write(self):
        assert_raises(NotImplementedError, self.datasource.read)
