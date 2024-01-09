  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)