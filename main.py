  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)