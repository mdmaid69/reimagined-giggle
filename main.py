  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)