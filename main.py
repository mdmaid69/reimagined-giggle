  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
def calculate_energy(mass, c=3*10**8):
        return mass * c**2