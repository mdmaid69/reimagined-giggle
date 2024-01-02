  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)