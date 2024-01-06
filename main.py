  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)