  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import math
def calculate_circle_area(radius):
        return math.pi * radius**2