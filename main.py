  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)