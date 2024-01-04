  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import math
def calculate_sign(x):
        return math.copysign(1, x)