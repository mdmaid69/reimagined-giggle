  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
def calculate_energy(mass, c=3*10**8):
        return mass * c**2