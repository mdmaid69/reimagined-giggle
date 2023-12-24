  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)