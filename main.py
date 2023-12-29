  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
import math
def calculate_factorial(n):
        return math.factorial(n)