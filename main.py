  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)