import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"