import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink