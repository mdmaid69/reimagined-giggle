  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)