  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())