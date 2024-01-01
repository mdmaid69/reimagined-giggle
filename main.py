  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()