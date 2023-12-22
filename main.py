  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
  def calculate_area_triangle(b, h):
        return 0.5 * b * h