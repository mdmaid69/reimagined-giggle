  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)