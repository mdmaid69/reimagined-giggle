  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)