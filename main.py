  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
def calculate_force(mass, acceleration):
        return mass * acceleration