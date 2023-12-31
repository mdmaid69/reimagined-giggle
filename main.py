  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)