import math
def calculate_sine(x):
        return math.sin(x)
  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns