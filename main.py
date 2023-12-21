  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()