import math
def calculate_floor(x):
        return math.floor(x)
  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime