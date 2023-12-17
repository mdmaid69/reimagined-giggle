  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)