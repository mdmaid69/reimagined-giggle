  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import math
def calculate_modulus(x, y):
        return math.fmod(x, y)