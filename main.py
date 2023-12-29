import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()