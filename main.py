  import os
  def get_current_directory():
        return os.getcwd()
def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5