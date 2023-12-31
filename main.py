  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)