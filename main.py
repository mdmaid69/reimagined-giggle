  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))