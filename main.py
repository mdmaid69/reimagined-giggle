  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)