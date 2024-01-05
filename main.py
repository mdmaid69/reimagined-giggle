  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)