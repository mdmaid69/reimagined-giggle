  import os
  def get_current_working_directory():
        return os.getcwd()
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)