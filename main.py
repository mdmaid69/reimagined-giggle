  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)