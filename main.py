import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags