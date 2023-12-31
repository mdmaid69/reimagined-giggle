import math
def calculate_gamma_function(x):
        return math.gamma(x)
  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks