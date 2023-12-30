  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)