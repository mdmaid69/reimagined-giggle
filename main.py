  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import math
def calculate_combinations(n, k):
        return math.comb(n, k)