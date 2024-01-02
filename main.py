import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()