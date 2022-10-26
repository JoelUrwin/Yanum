import argparse
from yanum import yanum
import os

def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')

def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", required=True, default=False, help="File input.", type=lambda x: is_valid_file(parser, x))
    args = parser.parse_args()

    yanum.Yanum(vars(args))