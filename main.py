  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)