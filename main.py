  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
def calculate_area_triangle(b, h):
        return 0.5 * b * h