import math
def calculate_absolute_value(x):
        return math.fabs(x)
  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev