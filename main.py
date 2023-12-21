  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
  def calculate_area_circle(r):
        return 3.14 * r**2