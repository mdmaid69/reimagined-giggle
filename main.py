  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
  def calculate_circumference_circle(r):
        return 2 * 3.14 * r