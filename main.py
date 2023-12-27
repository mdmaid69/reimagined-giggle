  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import math
def calculate_remainder(x, y):
        return math.remainder(x, y)