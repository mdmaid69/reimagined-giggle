  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
def calculate_perimeter_triangle(a, b, c):
        return a + b + c