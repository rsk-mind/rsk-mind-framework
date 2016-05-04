class Datasource(object):

    def __init__(self, path):
        self.path = path

    def read(self):
        """ """
        raise NotImplementedError("")

    def write(self, dataset):
        """ """
        raise NotImplementedError("")
