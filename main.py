  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
  def calculate_area_triangle(b, h):
        return 0.5 * b * h