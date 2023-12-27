import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)