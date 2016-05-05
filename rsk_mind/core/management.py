import argparse


def execute_from_command_line(argv):
    argv = argv[1:]

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('command', help='Command to execute!')
    parser.add_argument('project_name', help='')
    params = parser.parse_args(argv)

    if params.command == 'startapp':
        print 'Generate machine learning project'
    else:
        pass
