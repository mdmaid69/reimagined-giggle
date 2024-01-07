import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)