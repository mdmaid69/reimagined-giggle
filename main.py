  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)