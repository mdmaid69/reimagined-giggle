  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)