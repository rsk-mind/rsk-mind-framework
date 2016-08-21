class DataSource(object):

    def __init__(self, path):
        self.path = path

    def read(self):
        """Read a data source.

        Always place target class on last column.

        :return: a dataset
        """
        raise NotImplementedError("")

    def write(self, dataset, write_transformed=True):
        """Save data source

        Save on disk

        :param dataset:
        :param write_transformed:
        """
        raise NotImplementedError("")
