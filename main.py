import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns