  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
import math
def calculate_permutations(n, k):
        return math.perm(n, k)