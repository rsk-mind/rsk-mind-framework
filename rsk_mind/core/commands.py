import argparse
import json
import logging

from rsk_mind.classifier.xgboost_classifier import XGBoostClassifier
from rsk_mind.dataset import Statistics, Splitter

logging.basicConfig()
logger = logging.getLogger('rsk-mind')


def default_settings(setting):
    ANALYSIS = {
        'persist': False
    }

    if not hasattr(setting, 'ANALYSIS'):
        setattr(setting, 'ANALYSIS', ANALYSIS)

    return setting


def get_analytics(setting):
    """Calculate analytics on dataset and prints it.

    :param setting: project settings settings
    """
    logger.info('Reading dataset')
    DATASOURCE = setting.DATASOURCE
    datasource = DATASOURCE['IN']['class'](*DATASOURCE['IN']['params'])
    dataset = datasource.read()
    logger.info('Finish reading dataset')

    logger.info('Analysis on dataset')
    analytics = Statistics(dataset)
    logger.debug(analytics.statistics)
    logger.info('Finish analysis on dataset')

    if setting.ANALYSIS['persist']:
        logger.debug('Saving analysis')
        with open(setting.ANALYSIS['out'], 'w') as out:
            json.dump(analytics.statistics, out, indent=4, sort_keys=True)
        logger.debug('Complete saving analysis')
    else:
        logger.debug('Skip saving analysis')


def build_engine(setting):
    """Build a new rsk-mind engine.

    :param setting: project settings
    """
    logger.info('Starting building of new engine')
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

    logger.info('Finish building of new engine')


def run_engine(setting):
    """Start rsk-mind engine.

    :param setting: project settings
    """
    logger.info('Starting the %s engine' % setting.PROJECT_NAME)


def transformation(setting):
    """Transform dataset according the defined transformations.

    :param setting: project settings
    """
    DATASOURCE = setting.DATASOURCE

    datasource = DATASOURCE['IN']['class'](*DATASOURCE['IN']['params'])
    dataset = datasource.read()

    dataset.setTransformer(setting.TRANSFORMER())
    dataset.applyTransformations()

    datasource = DATASOURCE['OUT']['class'](*DATASOURCE['OUT']['params'])
    datasource.write(dataset)


def execute_from_command_line(argv, setting):
    """
    Controller of rsk_mind framework cli
    :param argv: cmd arguments
    :param setting: project settings
    """
    argv = argv[1:]

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('command', help='Command to execute!')
    parser.add_argument('--verbose', '-v', dest='verbose', action='store_true')
    params = parser.parse_args(argv)

    setting = default_settings(setting)

    if params.verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    if params.command == 'transformation':
        transformation(setting)
    elif params.command == 'build':
        build_engine(setting)
    elif params.command == 'run':
        run_engine(setting)
    elif params.command == 'analytics':
        get_analytics(setting)
    else:
        logger.error('%s: Not a valid command' % params.command)
