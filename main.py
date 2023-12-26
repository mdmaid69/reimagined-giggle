  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
def calculate_force(mass, acceleration):
        return mass * acceleration