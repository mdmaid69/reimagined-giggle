  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import math
def calculate_modulus(x, y):
        return math.fmod(x, y)