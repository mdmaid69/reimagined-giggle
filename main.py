  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
def calculate_area(radius):
        return 3.14 * radius * radius