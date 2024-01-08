  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3