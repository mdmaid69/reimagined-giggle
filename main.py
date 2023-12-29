  import os
  def split_path(path):
        return os.path.split(path)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)