  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3