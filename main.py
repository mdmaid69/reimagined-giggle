  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
def calculate_pressure(force, area):
        return force / area