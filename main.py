import math
def calculate_sign(x):
        return math.copysign(1, x)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)