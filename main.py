import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()