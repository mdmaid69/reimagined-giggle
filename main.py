  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))