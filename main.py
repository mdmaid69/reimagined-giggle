import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)