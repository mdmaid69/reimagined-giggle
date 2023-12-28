  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)