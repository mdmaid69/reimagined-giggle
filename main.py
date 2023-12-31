  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
def calculate_circumference_circle(r):
        return 2 * 3.14 * r