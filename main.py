  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
def calculate_area(radius):
        return 3.14 * radius * radius