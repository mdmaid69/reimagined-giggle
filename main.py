  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)