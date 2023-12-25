  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()