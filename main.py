import math
def calculate_error_function(x):
        return math.erf(x)
  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks