  import os
  def get_base_name(path):
        return os.path.basename(path)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2