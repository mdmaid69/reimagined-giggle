import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)