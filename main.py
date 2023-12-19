  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import math
def calculate_hyperbolic_arc_tangent(x):
        return math.atanh(x)