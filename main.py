  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import math
def calculate_exponential(x):
        return math.exp(x)