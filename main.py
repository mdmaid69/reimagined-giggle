  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2