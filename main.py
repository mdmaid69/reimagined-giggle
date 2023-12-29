  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)