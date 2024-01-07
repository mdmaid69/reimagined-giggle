import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)
  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime