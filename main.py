  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()