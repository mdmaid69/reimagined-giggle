import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()