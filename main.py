  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
def calculate_force(mass, acceleration):
        return mass * acceleration