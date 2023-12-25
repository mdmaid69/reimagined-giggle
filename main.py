  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))