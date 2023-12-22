  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3