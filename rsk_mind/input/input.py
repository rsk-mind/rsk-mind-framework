class Input():

    def __init__(self):
        pass

    def read(self):
        """ """
        raise NotImplementedError("")

    def transform(self, transformer, output=None):
        """ """
        raise NotImplementedError("")

    def classify(self, classifier, output=None):
        """ """
        raise NotImplementedError("")
