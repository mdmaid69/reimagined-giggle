  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()