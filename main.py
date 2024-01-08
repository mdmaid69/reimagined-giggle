  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)