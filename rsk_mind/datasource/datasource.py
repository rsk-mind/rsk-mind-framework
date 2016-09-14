class DataSource(object):

    def __init__(self, path):
        self.path = path

    def read(self):
        """
            Read a data source.

            Always place traget class on last column.
        """
        raise NotImplementedError("")

    def write(self, dataset):
        """ """
        raise NotImplementedError("")
