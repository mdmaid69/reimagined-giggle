  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)