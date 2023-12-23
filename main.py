  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()