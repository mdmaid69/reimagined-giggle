  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import math
def calculate_combinations(n, k):
        return math.comb(n, k)