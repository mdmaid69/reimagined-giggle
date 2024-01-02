import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)