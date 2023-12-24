import math
def calculate_combinations(n, k):
        return math.comb(n, k)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]