import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()