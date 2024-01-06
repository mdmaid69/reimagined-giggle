  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)