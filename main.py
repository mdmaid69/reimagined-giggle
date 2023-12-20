  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
  def calculate_area_circle(r):
        return 3.14 * r**2