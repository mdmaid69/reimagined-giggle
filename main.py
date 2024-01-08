  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2