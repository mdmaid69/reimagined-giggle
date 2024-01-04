  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
def calculate_pressure(force, area):
        return force / area