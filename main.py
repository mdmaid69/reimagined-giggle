  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)