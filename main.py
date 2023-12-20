  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)