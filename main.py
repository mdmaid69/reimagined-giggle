import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)
  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink