import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()