  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
def calculate_perimeter_triangle(a, b, c):
        return a + b + c