  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import math
def calculate_permutations(n, k):
        return math.perm(n, k)