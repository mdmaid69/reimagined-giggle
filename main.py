import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()