import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)