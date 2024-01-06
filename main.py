  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3