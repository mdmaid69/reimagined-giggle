  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
  def calculate_area_rectangle(l, w):
        return l * w