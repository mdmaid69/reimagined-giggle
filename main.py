import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()