import math
def calculate_sign(x):
        return math.copysign(1, x)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)