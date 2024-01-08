  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2