  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2