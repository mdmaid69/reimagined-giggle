  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)