  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)