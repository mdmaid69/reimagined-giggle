  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
def calculate_area_circle(r):
        return 3.14 * r**2