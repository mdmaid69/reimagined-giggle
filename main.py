  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)