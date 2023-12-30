  import os
  def get_base_name(path):
        return os.path.basename(path)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)