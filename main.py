  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3