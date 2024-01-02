  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
def calculate_perimeter_triangle(a, b, c):
        return a + b + c