  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
def calculate_perimeter_triangle(a, b, c):
        return a + b + c