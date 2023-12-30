  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)