  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)