import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid