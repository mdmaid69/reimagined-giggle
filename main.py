  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()