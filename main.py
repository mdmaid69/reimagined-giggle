  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
def calculate_area_circle(r):
        return 3.14 * r**2