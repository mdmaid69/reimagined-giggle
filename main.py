  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)