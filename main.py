  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)