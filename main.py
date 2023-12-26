import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]