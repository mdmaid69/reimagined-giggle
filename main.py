  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)