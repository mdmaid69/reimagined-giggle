  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import math
def calculate_hyperbolic_arc_cosine(x):
        return math.acosh(x)