import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)