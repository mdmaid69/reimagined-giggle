  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius