  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)