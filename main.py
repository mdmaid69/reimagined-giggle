import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)