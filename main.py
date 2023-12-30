  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)