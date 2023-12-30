  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)