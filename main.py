  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height