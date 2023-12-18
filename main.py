  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)