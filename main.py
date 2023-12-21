  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)