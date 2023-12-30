  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)