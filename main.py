  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)