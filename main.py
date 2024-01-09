import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)