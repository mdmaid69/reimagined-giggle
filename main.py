  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)