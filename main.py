  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import math
def calculate_sign(x):
        return math.copysign(1, x)