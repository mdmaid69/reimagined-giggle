  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)