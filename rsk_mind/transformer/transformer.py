class Transformer(object):
    """
        Base class for all transformer
    """

    class Feats:
        """
            Define feats on dataset
        """
        exclude = None

    def __init__(self):
        for field in self.get_feats():
            getattr(self.Feats, field).bind(field, self)

    def get_feats(self):
        """

        :return: a list of feats
        """
        return [x for x in dir(self.Feats) if not (x.startswith('__') or x in ['exclude'])]

    def get_transformer_func(self, feat_name):
        """

        :param feat_name: name of feat
        :return: a transformer function on feat
        """
        return getattr(self.Feats, feat_name).transform

    def get_excluded_feats(self):
        """

        :return: a list with excluded feats
        """
        return self.Feats.exclude
