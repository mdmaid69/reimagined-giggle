  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import math
def calculate_modulus(x, y):
        return math.fmod(x, y)