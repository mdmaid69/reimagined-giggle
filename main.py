import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)