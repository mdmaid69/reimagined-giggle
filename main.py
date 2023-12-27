  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3