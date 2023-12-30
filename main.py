  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import math
def calculate_sign(x):
        return math.copysign(1, x)