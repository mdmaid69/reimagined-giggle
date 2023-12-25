  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import math
def calculate_sign(x):
        return math.copysign(1, x)