from rsk_mind.engine import Engine


class HTTPEngine(Engine):
    def start(self):
        pass

    def build(self, setting, rebuild=False):

        setting = setting.TRAINING

        if setting['algorithm']['name'] == 'xgboost':
            params = setting['algorithm']['parameters']
            clf = XGBoostClassifier()

            DATASOURCE = setting['algorithm']['dataset']
            datasource = DATASOURCE['class'](*DATASOURCE['params'])
            _original_dataset = datasource.read()
            _original_dataset.applyTransformations()
            _splitter = Splitter(_original_dataset)

            clf.training_dataset = _splitter.training_dataset
            clf.validation_dataset = _splitter.validation_dataset
            clf.test_dataset = _splitter.test_dataset

            clf.train()
        else:
            logger.error('Unknown algorithm %s' % setting['algorithm'])

