  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5