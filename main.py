  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import math
def calculate_logarithm_base_2(x):
        return math.log2(x)