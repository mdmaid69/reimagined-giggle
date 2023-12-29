  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height