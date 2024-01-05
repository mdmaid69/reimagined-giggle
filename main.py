  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)