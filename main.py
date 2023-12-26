  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import math
def calculate_remainder(x, y):
        return math.remainder(x, y)