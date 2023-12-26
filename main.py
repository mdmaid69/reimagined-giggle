  import os
  def split_path(path):
        return os.path.split(path)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height