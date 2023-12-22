import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)