  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)