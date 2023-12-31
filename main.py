  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2