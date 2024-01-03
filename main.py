  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import math
def calculate_combinations(n, k):
        return math.comb(n, k)