  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import math
def calculate_permutations(n, k):
        return math.perm(n, k)