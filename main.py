import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime