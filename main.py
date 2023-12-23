import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height