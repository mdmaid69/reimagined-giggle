  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)