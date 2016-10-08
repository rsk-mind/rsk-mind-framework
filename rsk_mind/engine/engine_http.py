from rsk_mind.core.commands import logger
from rsk_mind.dataset import Splitter
from rsk_mind.engine import Engine
from rsk_mind.utils import get_datasource_from_setting


class HTTPEngine(Engine):
    def start(self):
        pass

    def build(self, setting, rebuild=False):

        setting = setting.TRAINING

        algorithms = setting['algorithms']

        for algorithm in algorithms:
            params = algorithm['parameters']
            clf = algorithm['classifier']

            datasource = get_datasource_from_setting(algorithm['dataset'])
            _original_dataset = datasource.read()
            _original_dataset.applyTransformations()
            _splitter = Splitter(_original_dataset)

            clf.training_dataset = _splitter.training_dataset
            clf.validation_dataset = _splitter.validation_dataset
            clf.test_dataset = _splitter.test_dataset

            clf.train()
        else:
            logger.error('Unknown algorithm %s' % setting['algorithm'])

