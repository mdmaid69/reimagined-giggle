  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)