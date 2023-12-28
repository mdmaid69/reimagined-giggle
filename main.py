import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius
  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid