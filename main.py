  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
  def calculate_circumference_circle(r):
        return 2 * 3.14 * r