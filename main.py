import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)