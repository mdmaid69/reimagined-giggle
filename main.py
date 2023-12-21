  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  def calculate_area_rectangle(l, w):
        return l * w