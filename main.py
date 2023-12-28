  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
def calculate_energy(mass, c=3*10**8):
        return mass * c**2