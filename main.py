import math
def calculate_sign(x):
        return math.copysign(1, x)
  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid