  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)