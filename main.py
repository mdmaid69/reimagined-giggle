  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import math
def calculate_permutations(n, k):
        return math.perm(n, k)