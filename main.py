  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)