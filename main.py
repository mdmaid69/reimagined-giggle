import math
def calculate_sign(x):
        return math.copysign(1, x)
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size