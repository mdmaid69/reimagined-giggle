  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import math
def calculate_logarithm_base_2(x):
        return math.log2(x)