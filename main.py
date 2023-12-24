  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
def calculate_area_triangle(b, h):
        return 0.5 * b * h