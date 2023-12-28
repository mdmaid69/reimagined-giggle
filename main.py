import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)