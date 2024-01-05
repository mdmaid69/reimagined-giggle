import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev