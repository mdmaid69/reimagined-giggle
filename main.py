  import os
  def get_current_working_directory():
        return os.getcwd()
def calculate_energy(mass, c=3*10**8):
        return mass * c**2