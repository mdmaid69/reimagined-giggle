  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)