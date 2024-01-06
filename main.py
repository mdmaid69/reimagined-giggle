import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]