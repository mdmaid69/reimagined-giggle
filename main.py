import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)