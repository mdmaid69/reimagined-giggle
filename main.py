  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)