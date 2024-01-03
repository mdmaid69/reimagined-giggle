  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()