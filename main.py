  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)