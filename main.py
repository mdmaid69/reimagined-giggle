  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import math
def calculate_logarithm(base, x):
        return math.log(x, base)