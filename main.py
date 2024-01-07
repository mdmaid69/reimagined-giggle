  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height