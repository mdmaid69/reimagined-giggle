  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)