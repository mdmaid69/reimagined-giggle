import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]