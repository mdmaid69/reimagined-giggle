  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)