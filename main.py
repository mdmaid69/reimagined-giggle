  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)