import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)