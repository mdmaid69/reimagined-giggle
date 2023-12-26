import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)