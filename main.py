  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"