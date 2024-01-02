  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)