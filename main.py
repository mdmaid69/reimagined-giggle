import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()