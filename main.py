  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import math
def calculate_combinations(n, k):
        return math.comb(n, k)