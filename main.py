  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)