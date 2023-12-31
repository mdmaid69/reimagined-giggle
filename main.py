import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()