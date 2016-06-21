import argparse, logging, json

from rsk_mind.dataset import Statistics

logging.basicConfig()
logger = logging.getLogger('rsk-mind')
logger.setLevel(logging.DEBUG)


def get_analytics(setting):

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
        logger.debug('Saving analysis on disk')
        with open(setting.ANALYSIS['out'], 'w') as out:
            json.dump(analytics.statistics, out, indent=4, sort_keys=True)
        logger.debug('Complete saving analysis on disk')
    else:
        logger.debug('Print on console analysis output')


def update_engine(setting):
    pass


def transformation(setting):
    DATASOURCE = setting.DATASOURCE

    datasource = DATASOURCE['IN']['class'](*DATASOURCE['IN']['params'])
    dataset = datasource.read()

    dataset.setTransformer(setting.TRANSFORMER())
    dataset.applyTransformations()

    datasource = DATASOURCE['OUT']['class'](*DATASOURCE['OUT']['params'])
    datasource.write(dataset)


def execute_from_command_line(argv, setting):
    argv = argv[1:]

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('command', help='Command to execute!')
    params = parser.parse_args(argv)

    if params.command == 'transformation':
        transformation(setting)
    elif params.command == 'update-engine':
        update_engine(setting)
    elif params.command == 'analytics':
        get_analytics(setting)