  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
def calculate_area_circle(r):
        return 3.14 * r**2