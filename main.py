  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
  def calculate_circumference_circle(r):
        return 2 * 3.14 * r