  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)