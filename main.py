  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)