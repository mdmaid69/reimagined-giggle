import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size