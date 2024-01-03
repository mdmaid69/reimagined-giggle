import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()