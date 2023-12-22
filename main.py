  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()