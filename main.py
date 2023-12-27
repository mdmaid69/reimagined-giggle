  import os
  def split_path(path):
        return os.path.split(path)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2