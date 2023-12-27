  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height