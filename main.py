  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
import math
def calculate_hyperbolic_arc_cosine(x):
        return math.acosh(x)