import sys

import argparse

def main(argv):

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument(
        'command', help='')
    parser.add_argument(
        'project_name', help='')
    # project_name/transformer.py
    # project_name/setting.py
    # project_name/manager.py
    params = parser.parse_args(argv)

    print params

if __name__ == "__main__":
   main(sys.argv[1:])
