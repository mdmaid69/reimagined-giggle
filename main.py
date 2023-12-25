  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)