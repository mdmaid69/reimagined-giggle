  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)