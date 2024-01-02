import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)