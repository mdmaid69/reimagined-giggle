  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
import math
def calculate_sign(x):
        return math.copysign(1, x)