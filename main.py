  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)