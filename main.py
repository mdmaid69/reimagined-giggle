  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)