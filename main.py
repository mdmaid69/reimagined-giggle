  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
  def calculate_perimeter_triangle(a, b, c):
        return a + b + c