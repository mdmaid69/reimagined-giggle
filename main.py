  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()