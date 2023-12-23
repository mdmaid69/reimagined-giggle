import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()