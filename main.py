  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)