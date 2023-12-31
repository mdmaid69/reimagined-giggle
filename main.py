  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)