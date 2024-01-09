  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3