import math
def calculate_error_function(x):
        return math.erf(x)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]