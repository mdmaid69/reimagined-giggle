  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import math
def calculate_factorial(n):
        return math.factorial(n)