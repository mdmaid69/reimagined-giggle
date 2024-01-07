  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)