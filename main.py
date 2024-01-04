  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import math
def calculate_combinations(n, k):
        return math.comb(n, k)