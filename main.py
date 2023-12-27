  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()