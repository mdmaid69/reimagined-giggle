  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)