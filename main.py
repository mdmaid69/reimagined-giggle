  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))