  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
def calculate_force(mass, acceleration):
        return mass * acceleration