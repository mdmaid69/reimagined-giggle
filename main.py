  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)