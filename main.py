  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)