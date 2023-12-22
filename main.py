import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()