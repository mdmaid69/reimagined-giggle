import math
def calculate_circle_area(radius):
        return math.pi * radius**2
  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime