  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height