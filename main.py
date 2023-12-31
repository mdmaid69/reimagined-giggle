  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import math
def calculate_hyperbolic_arc_tangent(x):
        return math.atanh(x)