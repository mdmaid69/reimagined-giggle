  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import random
def generate_random_number(start, end):
        return random.randint(start, end)