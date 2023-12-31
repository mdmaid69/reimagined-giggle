import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()