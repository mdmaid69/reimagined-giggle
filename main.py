  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)