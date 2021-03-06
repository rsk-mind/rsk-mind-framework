from .dataset import Dataset


class PandasDataset(Dataset):
    """ """

    def __init__(self, reader):
        """ """
        Dataset.__init__(self, None, None)
        self.reader = reader

    def setTransformer(self, transformer):
        """
        :param transformer:
        """
        self.transformer = transformer

    def applyTransformations(self):
        """ """
        for chunk in self.reader:
            if self.header is None:
                self.header = list(chunk.columns)
                for index, row in chunk.iterrows():
                    self.applyRowTransformation(list(row))

    def applyRowTransformation(self, row):
        """
        :param row:
        """
        if self.transformer is None:
            self.transformed_rows += [row]
            self.transformed_header = self.header
        else:
            transformed_row = []
            transformed_header = []

            for feat in self.transformer.get_feats():
                try:
                    i = self.header.index(feat)
                    trans_feat = self.transformer.get_transformer_func(feat)(row[i])
                except ValueError:
                    trans_feat = self.transformer.get_transformer_func(feat)(self.header, row)

                transformed_row += trans_feat

                if self.transformed_header is None:
                    if len(trans_feat) == 1:
                        transformed_header.append(feat)
                    else:
                        for j in range(len(trans_feat)):
                            transformed_header.append("%s_%s" % (feat, j))

            for i, feat in enumerate(self.header):
                if feat not in self.transformer.get_feats():
                    transformed_row.append(row[i])
                    transformed_header.append(feat)

            if self.transformed_header is None:
                self.transformed_header = transformed_header
            self.transformed_rows += [transformed_row]
