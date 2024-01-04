import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)