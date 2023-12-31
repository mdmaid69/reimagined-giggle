  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import math
def calculate_permutations(n, k):
        return math.perm(n, k)