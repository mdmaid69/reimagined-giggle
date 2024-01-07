import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"