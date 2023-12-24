  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
import math
def calculate_hyperbolic_sine(x):
        return math.sinh(x)