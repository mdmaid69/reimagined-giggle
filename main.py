  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()