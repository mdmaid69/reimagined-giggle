  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)