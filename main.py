import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)