import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)