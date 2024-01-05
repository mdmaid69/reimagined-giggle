  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
  def calculate_circumference_circle(r):
        return 2 * 3.14 * r