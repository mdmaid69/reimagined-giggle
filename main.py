import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)