  import os
  def get_directory_name(path):
        return os.path.dirname(path)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2