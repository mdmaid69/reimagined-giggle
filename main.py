import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)