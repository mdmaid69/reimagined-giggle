  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
  def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5