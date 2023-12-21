def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)