from abc import ABCMeta, abstractmethod


class DataSource(object):
    __metaclass__ = ABCMeta

    def __init__(self, path):
        self.path = path

    @abstractmethod
    def read(self):
        """Read a data source.

        Always place target class on last column.

        :return: a dataset
        """
        pass

    @abstractmethod
    def write(self, dataset, write_transformed=True):
        """Save data source

        Save on disk

        :param dataset:
        :param write_transformed:
        """
        pass
