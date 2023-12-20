  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2