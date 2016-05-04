class Dataset():

    def __init__(self, header, rows):
        self.header = header
        self.rows = rows
        self.transformer = None
        self.transformed_rows = []
        self.transformed_header = []

    def setTransformer(self, transformer):
        self.transformer = transformer

    def applyTransformations(self):
        """ """
        raise NotImplementedError("")

    def applyRowTransformation(self, row):
        """ """
        raise NotImplementedError("")
