  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
def calculate_energy(mass, c=3*10**8):
        return mass * c**2