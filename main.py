  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)