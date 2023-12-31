  def calculate_circumference_circle(r):
        return 2 * 3.14 * r
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()