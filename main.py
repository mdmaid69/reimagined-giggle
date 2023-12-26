  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import math
def calculate_modulus(x, y):
        return math.fmod(x, y)