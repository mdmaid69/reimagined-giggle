  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"