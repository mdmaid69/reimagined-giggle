  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
def calculate_energy(mass, c=3*10**8):
        return mass * c**2