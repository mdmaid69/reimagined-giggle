  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())