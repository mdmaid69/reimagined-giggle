  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)