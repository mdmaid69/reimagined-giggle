  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import math
def calculate_circle_area(radius):
        return math.pi * radius**2