import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
  import os
  def split_path(path):
        return os.path.split(path)