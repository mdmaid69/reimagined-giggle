  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import math
def calculate_logarithm_base_2(x):
        return math.log2(x)