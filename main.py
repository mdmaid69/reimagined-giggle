import math
def calculate_sign(x):
        return math.copysign(1, x)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)