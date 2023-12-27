import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value