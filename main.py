  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2