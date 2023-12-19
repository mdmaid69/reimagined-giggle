  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
def calculate_area(radius):
        return 3.14 * radius * radius