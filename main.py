import math
def calculate_tangent(x):
        return math.tan(x)
  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns