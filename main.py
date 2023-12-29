  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)