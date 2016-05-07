import argparse, os


def transformation(setting):
    DATASOURCE = setting.DATASOURCE

    datasource = DATASOURCE['IN']['class'](*DATASOURCE['IN']['params'])
    dataset = datasource.read()

    datasource = DATASOURCE['OUT']['class'](*DATASOURCE['OUT']['params'])
    datasource.write(dataset)


def execute_from_command_line(argv, setting):
    argv = argv[1:]

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('command', help='Command to execute!')
    params = parser.parse_args(argv)

    if params.command == 'transformation':
        transformation(setting)
    else:
        pass
