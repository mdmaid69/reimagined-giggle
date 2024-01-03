import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()