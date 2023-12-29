import math
def calculate_combinations(n, k):
        return math.comb(n, k)
  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime