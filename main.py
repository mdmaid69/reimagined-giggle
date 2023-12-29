import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()