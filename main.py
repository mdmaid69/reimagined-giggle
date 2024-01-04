  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()