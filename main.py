  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()