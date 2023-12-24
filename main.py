  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)