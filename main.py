  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)