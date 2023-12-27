  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()