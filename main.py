  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)