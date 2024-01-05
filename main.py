  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)