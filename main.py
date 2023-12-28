def calculate_force(mass, acceleration):
        return mass * acceleration
  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink