import math
def calculate_arc_tangent(x):
        return math.atan(x)
  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink