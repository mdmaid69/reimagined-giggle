import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size