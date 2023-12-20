import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)