  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius