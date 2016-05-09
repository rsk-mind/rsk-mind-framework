class Dataset():
    """ """

    def __init__(self, header, rows):
        """ """
        self.header = header
        self.rows = rows
        self.transformer = None
        self.transformed_rows = []
        self.transformed_header = None

    def setTransformer(self, transformer):
        """ """
        self.transformer = transformer

    def applyTransformations(self):
        """ """
        for row in self.rows:
            self.applyRowTransformation(row)

    def applyRowTransformation(self, row):
        """ """
        if self.transformer == None:
            transformed_row = row
            transformed_header = self.header
        else:
            transformed_row = []
            transformed_header = []

            for feat in self.transformer.get_fields():
                try:
                    i = self.header.index(feat)
                    trans_feat = getattr(self.transformer.Fields, feat).transform(row[i])

                    if self.transformed_header is None:
                        if len(trans_feat) == 1:
                            transformed_header.append(feat)
                        else:
                            for j in range(len(transformed_feat)):
                                transformed_header.append("%s_%s" % (feat, j))

                    transformed_row += transformed_feat
                except:
                    # composite feat
                    pass

        if self.transformed_header is None:
            self.transformed_header = transformed_header
        self.transformed_rows += [transformed_row]
