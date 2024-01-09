import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)
  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns