  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import math
def calculate_circle_area(radius):
        return math.pi * radius**2