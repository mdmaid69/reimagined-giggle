  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2