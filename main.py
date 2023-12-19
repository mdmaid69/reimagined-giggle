  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)