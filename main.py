  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height