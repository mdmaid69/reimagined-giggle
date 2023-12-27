  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
  def calculate_area_circle(r):
        return 3.14 * r**2