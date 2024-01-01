  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())