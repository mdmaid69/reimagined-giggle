  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()