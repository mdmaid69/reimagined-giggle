import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
import itertools
print(list(itertools.permutations([1, 2, 3])))