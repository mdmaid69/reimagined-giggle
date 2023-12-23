  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))