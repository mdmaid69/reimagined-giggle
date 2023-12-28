  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
  def calculate_area_circle(r):
        return 3.14 * r**2