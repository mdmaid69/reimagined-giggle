  import os
  def delete_file(file_name):
        os.remove(file_name)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2