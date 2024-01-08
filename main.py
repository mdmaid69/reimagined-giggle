import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)