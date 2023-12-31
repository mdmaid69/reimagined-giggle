import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
  import os
  def delete_file(file_name):
        os.remove(file_name)