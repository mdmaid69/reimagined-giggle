  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import math
def calculate_sign(x):
        return math.copysign(1, x)