  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)