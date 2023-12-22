  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)