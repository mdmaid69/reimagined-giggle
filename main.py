  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
import math
def calculate_factorial(n):
        return math.factorial(n)