  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import math
def calculate_modulus(x, y):
        return math.fmod(x, y)