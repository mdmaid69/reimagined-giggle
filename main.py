  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3