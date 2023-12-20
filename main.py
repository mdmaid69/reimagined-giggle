  import os
  def split_path(path):
        return os.path.split(path)
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)