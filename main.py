  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
  def calculate_area_rectangle(l, w):
        return l * w