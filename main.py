  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)