import math
def calculate_ceiling(x):
        return math.ceil(x)
  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns