  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import math
def calculate_remainder(x, y):
        return math.remainder(x, y)