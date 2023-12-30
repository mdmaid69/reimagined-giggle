  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)