  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
def calculate_area_rectangle(l, w):
        return l * w