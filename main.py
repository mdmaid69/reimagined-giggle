  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)