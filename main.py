import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)