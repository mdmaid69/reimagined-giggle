  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()