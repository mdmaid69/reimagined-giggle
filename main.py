import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)