  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))