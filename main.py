import math
def calculate_permutations(n, k):
        return math.perm(n, k)
  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns