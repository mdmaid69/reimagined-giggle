  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
def calculate_perimeter_triangle(a, b, c):
        return a + b + c