  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))