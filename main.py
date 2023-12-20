  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2