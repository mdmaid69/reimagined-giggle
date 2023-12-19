  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import math
def calculate_hyperbolic_arc_cosine(x):
        return math.acosh(x)