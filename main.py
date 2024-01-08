import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size