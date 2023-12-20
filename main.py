  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)