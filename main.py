  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)