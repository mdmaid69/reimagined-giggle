  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
  def calculate_circumference_circle(r):
        return 2 * 3.14 * r