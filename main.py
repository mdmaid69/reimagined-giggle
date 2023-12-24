  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height