  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import math
def calculate_logarithm(base, x):
        return math.log(x, base)