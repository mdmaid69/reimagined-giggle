  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
import math
def calculate_exponential(x):
        return math.exp(x)