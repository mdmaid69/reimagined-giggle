  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)