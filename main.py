  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2