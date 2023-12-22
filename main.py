  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)