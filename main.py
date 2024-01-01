  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)