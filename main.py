  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height