  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)