  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height