  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)