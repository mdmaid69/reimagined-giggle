  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
  def calculate_area_triangle(b, h):
        return 0.5 * b * h