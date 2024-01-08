  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import math
def calculate_logarithm_base_2(x):
        return math.log2(x)