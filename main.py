  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
def calculate_circumference_circle(r):
        return 2 * 3.14 * r