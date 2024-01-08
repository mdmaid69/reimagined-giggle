import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()