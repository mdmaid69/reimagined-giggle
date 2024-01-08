  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3