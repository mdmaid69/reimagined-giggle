  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)