import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino