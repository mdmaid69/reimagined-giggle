  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height