  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)