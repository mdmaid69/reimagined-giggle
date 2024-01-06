  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))