  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
def calculate_area_rectangle(l, w):
        return l * w