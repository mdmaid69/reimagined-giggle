  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)