import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]