class Transformer(object):
    class Feats():
        exclude = None

    def __init__(self):
        for field in self.get_feats():
            getattr(self.Feats, field).bind(field, self)

    def get_feats(self):
        return [x for x in dir(self.Feats) if not (x.startswith('__') or x in ['exclude'])]

    def get_transformer_func(self, feat_name):
        return getattr(self.Feats, feat_name).transform
