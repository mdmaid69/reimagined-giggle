  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
def find_unique_words(sentence):
        return set(sentence.split())