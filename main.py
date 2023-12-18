  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius