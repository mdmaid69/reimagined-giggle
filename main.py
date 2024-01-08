  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)