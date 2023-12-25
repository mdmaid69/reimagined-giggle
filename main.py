import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)