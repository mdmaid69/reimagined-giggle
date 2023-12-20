import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)