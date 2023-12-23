import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)