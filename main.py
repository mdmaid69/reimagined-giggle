  import os
  def split_path(path):
        return os.path.split(path)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)