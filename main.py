  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()