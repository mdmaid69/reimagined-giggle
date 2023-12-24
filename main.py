import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)