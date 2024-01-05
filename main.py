  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))