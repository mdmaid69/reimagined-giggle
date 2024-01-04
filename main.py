  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
def calculate_area_triangle(b, h):
        return 0.5 * b * h