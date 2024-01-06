  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)