  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import math
def calculate_modulus(x, y):
        return math.fmod(x, y)