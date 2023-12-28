  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)